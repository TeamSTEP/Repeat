# cardgame.rpy - Cardgame support for Ren'Py
# Copyright (C) 2008 PyTom <pytom@bishoujo.us>
#
# This software may be distributed in modified or unmodified form,
# provided:
#
# (1) This complete license notice is retained.
#
# (2) This software and all software and data files distributed
# alongside this software and intended to be loaded in the same
# memory space may be redistributed without requirement for
# payment, notification, or other forms of compensation.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#
# Commercial licensing for this software is available, please
# contact pytom@bishoujo.us for information.

init python:

    import pygame
    
    DRAG_NONE = 0
    DRAG_CARD = 1
    DRAG_ABOVE = 2
    DRAG_STACK = 3
    DRAG_TOP = 4

    # Returns the overlap of the area between the two
    # rectangles.
    def __rect_overlap_area(r1, r2):
        if r1 is None or r2 is None:
            return 0
        
        x1, y1, w1, h1 = r1
        x2, y2, w2, h2 = r2

        maxleft = max(x1, x2)
        minright = min(x1 + w1, x2 + w2)
        maxtop = max(y1, y2)
        minbottom = min(y1 + h1, y2 + h2)

        if minright < maxleft:
            return 0

        if minbottom < maxtop:
            return 0

        return (minright - maxleft) * (minbottom - maxtop)

    def __default_can_drag(table, stack, card):
        return table.get_faceup(card)
    
    class Table(renpy.Displayable):

        def __init__(self, back=None, base=None, springback=0.1, rotate=0.1, can_drag=__default_can_drag, doubleclick=.33, **kwargs):

            renpy.Displayable.__init__(self, **kwargs)
            
            # A map from card value to the card object corresponding to
            # that value.
            self.cards = { }

            # A list of the stacks that have been defined.
            self.stacks = [ ]

            # The back of cards that don't have a more specific back
            # defined.
            self.back = renpy.easy.displayable_or_none(back)

            # The base of stacks that don't have a more specific base
            # defined.
            self.base = renpy.easy.displayable_or_none(base)

            # The amount of time it takes for cards to springback
            # into their rightful place.
            self.springback = springback

            # The amount of time it takes for cards to rotate into
            # their proper orientation.
            self.rotate = rotate

            # A function that is called to tell if we can drag a
            # particular card.
            self.can_drag = can_drag

            # The time between clicks for the click to be considered a
            # double-click.
            self.doubleclick = doubleclick

            # Are we sensitive to input? [doc]
            self.sensitive = True
            
            # The last click event.
            self.last_event = CardEvent()
            
            # The card that has been clicked.
            self.click_card = None

            # The stack that has been clicked.
            self.click_stack = None
            
            # The list of cards that are being dragged.
            self.drag_cards = [ ]
            
            # Are we dragging the cards?
            self.dragging = False
            
            # The position where we clicked.
            self.click_x = 0
            self.click_y = 0
            
            # The amount of time we've been shown for.
            self.st = 0

        # This shows the table on the given layer.
        def show(self, layer='master'):

            for v in self.cards.itervalues():
                v.offset = __Fixed(0, 0)

            ui.layer(layer)
            ui.add(self)
            ui.close()

        # This hides the table.
        def hide(self, layer='master'):
            ui.layer(layer)
            ui.remove(self)
            ui.close()

        # This controls sensitivity.
        def set_sensitive(self, value):
            self.sensitive = value
            
        def get_card(self, value):
            if value not in self.cards:
                raise Exception("No card has the value %r." % value)

            return self.cards[value]
            
        # This sets the faceup status of a card.
        def set_faceup(self, card, faceup=True):
            self.get_card(card).faceup = faceup
            renpy.redraw(self, 0)

        def get_faceup(self, card):
            return self.get_card(card).faceup
            
        # This sets the rotation of a card.
        def set_rotate(self, card, rotation):
            __Rotate(self.get_card(card), rotation)
            renpy.redraw(self, 0)

        def get_rotate(self, card):
            return self.get_card(card).rotate.rotate_limit()
            
        def add_marker(self, card, marker):
             self.get_card(card).markers.append(marker)
             renpy.redraw(self, 0)

        def remove_marker(self, card, marker):
            self.get_card(card).markers.remove(marker)
            renpy.redraw(self, 0)

        # Called to create a new card.
        def card(self, value, face, back=None):
            self.cards[value] = __Card(self, value, face, back)

        # Called to create a new stack.
        def stack(self, x, y, xoff=0, yoff=0, show=1024, base=None,
                  click=False, drag=DRAG_NONE, drop=False, hidden=False):

            rv = __Stack(self, x, y, xoff, yoff, show, base, click, drag, drop, hidden) 
            
            self.stacks.append(rv)
            return rv

        # Force a redraw on each interaction.
        def per_interact(self):
            renpy.redraw(self, 0)

        
        def render(self, width, height, st, at):

            self.st = st

            rv = renpy.Render(width, height)

            for s in self.stacks:

                if s.hidden:
                    s.rect = None
                    for c in s.cards:
                        c.rect = None
                    continue

                s.render_to(rv, width, height, st, at)
                
                for c in s.cards:
                    c.render_to(rv, width, height, st, at)
            
            return rv

        def event(self, ev, x, y, st):

            self.st = st

            if not self.sensitive:
                return

            grabbed = renpy.display.focus.get_grab()

            if (grabbed is not None) and (grabbed is not self):
                return
            
            if ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1:

                if self.click_stack:
                    return

                stack = None
                card = None
                
                for s in self.stacks:

                    sx, sy, sw, sh = s.rect
                    if sx <= x and sy <= y and sx + sw > x and sy + sh > y:
                        stack = s


                    for c in s.cards[-s.show:]:
                        if c.rect is None:
                            continue

                        cx, cy, cw, ch = c.rect
                        if cx <= x and cy <= y and cx + cw > x and cy + ch > y:
                            card = c
                            stack = c.stack
                            
                if stack is None:
                    return

                # Grab the display.
                renpy.display.focus.set_grab(self)
                
                # Don't let the user grab a moving card.
                if card is not None:
                    xoffset, yoffset = card.offset.offset()
                    if xoffset or yoffset:
                        return
                    
                # Move the stack containing the card to the front.
                self.stacks.remove(stack)
                self.stacks.append(stack)
                
                if stack.click or stack.drag:
                    self.click_card = card
                    self.click_stack = stack
                
                if card is None or not self.can_drag(self, card.stack, card.value):
                    self.drag_cards = [ ]
                elif card.stack.drag == DRAG_CARD:
                    self.drag_cards = [ card ]
                elif card.stack.drag == DRAG_ABOVE:
                    self.drag_cards = [ ]
                    for c in card.stack.cards:
                        if c is card or self.drag_cards:
                            self.drag_cards.append(c)
                elif card.stack.drag == DRAG_STACK:
                    self.drag_cards = list(card.stack.cards)
                elif card.stack.drag == DRAG_TOP:
                    if card.stack.cards[-1] is card:
                        self.drag_cards = [ card ]
                    else:
                        self.drag_cards = [ ]

                for c in self.drag_cards:
                    c.offset = __Fixed(0, 0)
                        
                self.click_x = x
                self.click_y = y
                self.dragging = False
                
                renpy.redraw(self, 0)
                
                raise renpy.IgnoreEvent()

            if ev.type == pygame.MOUSEMOTION or (ev.type == pygame.MOUSEBUTTONUP and ev.button == 1):

                if abs(x - self.click_x) > 7 or abs(y - self.click_y) > 7:
                    self.dragging = True

                dx = x - self.click_x
                dy = y - self.click_y

                for c in self.drag_cards:
                    xoffset, yoffset = c.offset.offset()
                    
                    cdx = dx - xoffset
                    cdy = dy - yoffset

                    c.offset = __Fixed(dx, dy)
                    
                    if c.rect:
                        cx, cy, cw, ch = c.rect
                        cx += cdx
                        cy += cdy
                        c.rect = (cx, cy, cw, ch)

                area = 0
                dststack = None 
                dstcard = None
                
                for s in self.stacks:
                    if not s.drop:
                        continue
                    
                    for c in self.drag_cards:

                        if c.stack == s:
                            continue
                        a = __rect_overlap_area(c.rect, s.rect)
                        if a >= area:
                            dststack = s
                            dstcard = None
                            area = a
                            
                        for c1 in s.cards:
                            a = __rect_overlap_area(c.rect, c1.rect)
                            if a >= area:
                                dststack = s
                                dstcard = c1
                                area = a

                if area == 0:
                    dststack = None
                    dstcard = None

                renpy.redraw(self, 0)

                if ev.type == pygame.MOUSEMOTION:
                    raise renpy.IgnoreEvent()

            if ev.type == pygame.MOUSEBUTTONUP and ev.button == 1:

                # Ungrab the display.
                renpy.display.focus.set_grab(None)

                evt = None

                if self.dragging:
                    if dststack is not None and self.drag_cards:

                        evt = CardEvent()
                        evt.type = "drag"
                        evt.table = self
                        evt.stack = self.click_stack
                        evt.card = self.click_card.value
                        evt.drag_cards = [c.value for c in self.drag_cards]
                        evt.drop_stack = dststack
                        if dstcard:
                            evt.drop_card = dstcard.value
                        evt.time = st
                            
                else:

                    if self.click_stack.click:                    

                        evt = CardEvent()
                        evt.type = "click"
                        evt.table = self
                        evt.stack = self.click_stack
                        if self.click_card:
                            evt.card = self.click_card.value
                        else:
                            evt.card = None

                        evt.time = st

                        if (evt.type == self.last_event.type
                            and evt.stack == self.last_event.stack
                            and evt.card == self.last_event.card
                            and evt.time < self.last_event.time + self.doubleclick):

                            evt.type = "doubleclick"

                if evt is not None:
                    self.last_event = evt
                        
                for c in self.drag_cards:
                    c.springback()
                    
                self.click_card = None
                self.click_stack = None
                self.drag_cards = [ ]

                if evt is not None: 
                    return evt
                else:
                    raise renpy.IgnoreEvent()

                
    class CardEvent(object):

        def __init__(self):
            self.type = None
            self.stack = None
            self.card = None
            self.drag_cards = None
            self.drop_stack = None
            self.drop_card = None
            self.time = 0
            
    # Represents a stack of one or more cards, which can be placed on the
    # table.
    class __Stack(object):

        def __init__(
            self, table,
            x, y,
            xoff, yoff,
            show, base,
            click, drag, drop,
            hidden):


            # The table this stack belongs to.
            self.table = table

            # The x and y coordinates of the center of the top card of
            # this stack.
            self.x = x
            self.y = y

            # The offset in the x and y directions of each successive
            # card.
            self.xoff = xoff
            self.yoff = yoff

            # The number of cards to show from this stack. (We show the
            # last show cards if this is less than the numebr of cards
            # in the stack.)
            self.show = show

            # The image that is shown behind the stack. If None, the
            # background is taken from the table.
            self.base = base

            # Should we report click events on this stack?
            self.click = click

            # Should we allow dragging this stack? If so, how?
            self.drag = drag

            # Should we allow dropping to this stack?
            self.drop = drop

            # Is this stack hidden?
            self.hidden = hidden
            
            # The list of cards in this stack.
            self.cards = [ ]

            # The rectangle for the background of this effect.
            self.rect = None
            
        def insert(self, index, card):
            card = self.table.get_card(card)

            if card.stack:
                card.stack.cards.remove(card)

            card.stack = self
            self.cards.insert(index, card)

            self.table.stacks.remove(self)
            self.table.stacks.append(self)
            
            card.springback()
            
        def append(self, card):
            if card in self.cards:                
                self.insert(len(self.cards) - 1, card)
            else:
                self.insert(len(self.cards), card)

        def remove(self, card):
            card = self.table.get_card(card)            
            self.cards.remove(card)
            card.stack = None
            card.rect = None

        def deal(self):
            if not self.cards:
                return None
                
            card = self.cards[-1]
            self.remove(card.value)
            return card.value

        def shuffle(self):
            renpy.random.shuffle(self.cards)
            renpy.redraw(self.table, 0)
            
        def __len__(self):
            return len(self.cards)

        def __getitem__(self, idx):
            return self.cards[idx].value

        def __iter__(self):
            for i in self.cards:
                yield i.value

        def __contains__(self, item):
            return self.table.get_card(card) in self.cards
                
        def render_to(self, rv, width, height, st, at):

            base = self.base or self.table.base

            if base is None:
                return

            surf = renpy.render(base, width, height, st, at)
            cw, ch = surf.get_size()

            cx = self.x - cw / 2
            cy = self.y - ch / 2

            self.rect = (cx, cy, cw, ch)
            rv.blit(surf, (cx, cy))
            
    class __Card(object):

        def __init__(self, table, value, face, back):

            # The table this card belongs to.
            self.table = table

            # The value of this card.
            self.value = value

            # The face of this card.
            self.face = renpy.easy.displayable(face)

            # The back of this card. If None, then the back is taken from
            # the table the card belongs to.
            self.back = renpy.easy.displayable_or_none(back)

            # Is this card faceup (or face down?)
            self.faceup = True

            # Object that's called to decide how rotated this card should
            # be.
            self.rotate = None

            # A series of highlights that should be drawn over this card.
            self.highlights = [ ]

            # The stack this card is in.
            self.stack = None

            # An object that gives the offset of this card relative to
            # where it would normally be placed.
            self.offset = __Fixed(0, 0)
            
            # The rectangle where this card was last drawn to the screen
            # at.
            self.rect = None

            __Rotate(self, 0)
            
        # Returns the base x and y placement of this card.
        def place(self):
            s = self.stack
            offset = max(len(s.cards) - s.show, 0)
            index = max(s.cards.index(self) - offset, 0)

            return (s.x + s.xoff * index, s.y + s.yoff * index)

        def springback(self):
            if self.rect is None:
                self.offset = __Fixed(0, 0)
            else:
                self.offset = __Springback(self)
                        
        def render_to(self, rv, width, height, st, at):
            
            x, y = self.place()
            xoffset, yoffset = self.offset.offset()
            x += xoffset
            y += yoffset

            if self.faceup:
                d = self.face
            else:
                d = self.back or self.table.back
                
            # TODO: Figure out if we can reuse some of this.

            if self.highlights:
                d = Fixed(* ([d] + [renpy.easy.displayable(i) for i in self.highlights]))

            r = self.rotate.rotate()
            if r:
                d = RotoZoom(r, r, 0, 1, 1, 0)(d)
                
            surf = renpy.render(d, width, height, st, at)
            w, h = surf.get_size()

            x -= w / 2
            y -= h / 2

            self.rect = (x, y, w, h)

            rv.blit(surf, (x, y))
            
        def __repr__(self):
            return "<__Card %r>" % self.value
        

    class __Springback(object):

        def __init__(self, card):
            self.card = card
            self.table = table = card.table
            
            self.start = table.st

            cx, cy, cw, ch = self.card.rect
            x = cx + cw / 2
            y = cy + ch / 2

            self.startx = x
            self.starty = y

        def offset(self):

            t = (self.table.st - self.start) / self.table.springback
            t = min(t, 1.0)
            
            if t < 1.0:
                renpy.redraw(self.table, 0)

            px, py = self.card.place() 
                
            return int((self.startx - px) * (1.0 - t)), int((self.starty - py) * (1.0 - t))


    class __Fixed(object):
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def offset(self):
            return self.x, self.y
        

    class __Rotate(object):
        def __init__(self, card, amount):

            self.table = table = card.table
            self.start = table.st
            
            if card.rotate is None:
                self.start_rotate = amount
            else:
                self.start_rotate = card.rotate.rotate()

            self.end_rotate = amount

            card.rotate = self

            
        def rotate(self):

            if self.start_rotate == self.end_rotate:
                return self.start_rotate

            t = (self.table.st - self.start) / self.table.springback
            t = min(t, 1.0)

            if t < 1.0:
                renpy.redraw(self.table, 0)

            return self.start_rotate + (self.end_rotate - self.start_rotate) * t
        
        def rotate_limit(self):
            return self.end_rotate



#########################################################################
#########################################################################
#########################################################################
# $ myClock.add_time(시간,분,애니메이션이 바뀌는데 걸리는 시간) 시간을 추가
# $ myClock.set_time(시간,분) 시간 변경
# $ myClock.set_alarm(시간,분,True/False) 알람 설정
# $ myClock.second_hand_visible = True/False 초침 표시/표시 안 함
# $ myClock.runmode("auto"/"real"/"none", True/False) 시계 표시 모드
# $ myClock.analogue = True/False 아날로그 시계 모드 설정


init -1 python:
    from datetime import datetime #This is to get the real world datetime
    
    img = ["system/VintageClockBase450x450.png", "system/VintageClockHour450x450.png", "system/VintageClockMinute450x450.png", "system/VintageClockSecond400x400.png", "system/DigitalClockBase460x200.png"]
    """
    Use your own clock images here, or use the ones I provided.
    Note: your analogue clock images need to be square, your digital base can be any size but keeping it close 
    to the ratio of 460x200 gives the best results.
    Important: You should have four images listed in this order--The Analogue Clock Base, The Hour Hand, The Minute Hand, The Second Hand, The Digital Clock Base
    """
    renpy.music.register_channel("TockBG", mixer= "sfx", loop=True)
    renpy.music.register_channel("ChimeBG", mixer= "sfx", loop=False, tight=True) 
    renpy.music.register_channel("Alarm", mixer= "sfx", loop=False, tight=True)   
    """These are here so that the various clock sounds play on their own sound channels."""
    
    """As a Creater Defined Displayable this needs to extend the Displayable class)"""
    class Clock(renpy.Displayable):
        
        #The clock class constructor
        def __init__(self, ana=True, h=0, m=0, resize=150, sH=True, **kwargs):
            """
            This constructor takes the following arguments:
            ana = True gives the analogue version of the clock, False gives the digital version
            h=Hours the clock should start on
            m=Minutes the clock should start on
            resize=How big you want your clock images to be
            sH=If you want the second hand to be visible or not
            If you do not give any arguments when you create the clock, it will default to
             a clock with 0 hours, 0 minutes, 150 pixels square, with a second hand showing
            """
            super(Clock, self).__init__(**kwargs)
            
            #These lines are for setting up the images used and the size of them
            self.width = resize
            self.d_height = (resize*32)/100
            self.base_image = im.Scale(img[0], resize, resize)
            self.hour_hand_image = im.Scale(img[1], resize, resize)
            self.minute_hand_image = im.Scale(img[2], resize, resize)
            self.second_hand_image = im.Scale(img[3], resize, resize)
            self.digital_base_image = im.Scale("system/DigitalClockBase460x200.png", self.width, self.d_height)
            self.offset = (resize*2**0.5-resize)/2
            self.second_hand_visible = sH
 
            #Variables for handling time
            self.minutes = (h*60)+m 
            self.seconds = self.minutes*60
            self.seconds_target = 0 
            self.step = 0 
            self.old_second = None #Used in autorun
            self.alarm_hr = 0
            self.alarm_min = 0
            
            #Variables for determining the clock modes
            self.analogue = ana
            self.auto_run = False
            self.realtime_run = False

            #Variables for handling sound
            self.second_sound_on = False
            self.chime_on = False
            self.last_minute = 0 #Used for chimes
            self.play_chime = False #Chimes are currenlty running or not
            self.alarm_on = False
            self.play_alarm = False #Used for chimes
            
            #Variables for the Style of the font used by the Digital Clock
            style.digi_clock = Style(style.default)
            style.digi_clock.font = "fonts/DigitalRegular.ttf"
            style.digi_clock.color = "#f00"
            style.digi_clock.size = self.d_height * 0.8
            style.digi_clock.yalign = 0.5
        
        # Function that continuously updates the graphics of the clock
        def render(self, width, height, st, at):
            
            #Advances the seconds variable until it is the same as the seconds_target variable
            if self.seconds_target > self.seconds:
                self.seconds += self.step
            
            #Resets the seconds_target variable
            if self.seconds_target == self.seconds:
                self.seconds_target = 0
                
            #Makes sure the minutes variable is always in sync with the seconds variable
            if self.minutes != self.seconds//60:
                self.minutes = self.seconds//60
            
            #This is all the render information for the Analogue Clock
            if self.analogue:                
                # Create transform to rotate the second hand
                tM = Transform(child=self.minute_hand_image, rotate=self.seconds*0.1, subpixel=True)
                tH = Transform(child=self.hour_hand_image, rotate=self.seconds*0.0083, subpixel=True)

                # Create a render for the children.
                base_render = renpy.render(self.base_image, width, height, st, at)
                minute_render = renpy.render(tM, width, height, st, at)
                hour_render = renpy.render(tH, width, height, st, at)
            
                #If we are in chime_run mode, checks to see the chimes need to be rung
                if self.chime_on == True:
                    if self.last_minute != self.minutes:
                        self.play_chime = False
                        self.last_minute = self.minutes
                    self.start_chime()

                # Create the render we will return.
                render = renpy.Render(self.width, self.width)

                # Blit (draw) the child's render to our render.
                render.blit(base_render, (0, 0))
                render.blit(minute_render, (-self.offset, -self.offset))
                render.blit(hour_render, (-self.offset, -self.offset))
                
                #If the second hand is visible, this renders the second hand, transforms it and adds it to our clock
                if self.second_hand_visible:
                    tS = Transform(child=self.second_hand_image, rotate=self.seconds*6, subpixel=True)
                    sec_render = renpy.render(tS, width, height, st, at)
                    render.blit(sec_render, (-self.offset, -self.offset))
            #This is all hte render information for the Digital Clock
            else:
                # create the text that will go in the Digital Clock and the boxes that text will sit in 
                col =Text(":", style="digi_clock")  
                time = list(Text("{0:02d}".format(item), style="digi_clock") for item in self.get_time())
                fxsize = (self.width-10)//4
                
                # Determine what to display based on if the seconds are  visible
                if self.second_hand_visible:
                    digi_text = HBox(Fixed(time[0], xsize=fxsize), col, Fixed(time[1], xsize=fxsize), col, Fixed(time[2], xsize=fxsize), xalign=0.5)
                else:
                    digi_text = HBox(Fixed(time[0], xsize=fxsize), col, Fixed(time[1], xsize=fxsize), xalign=0.5)
                
                #Put all of our pieces into one Fixed Box
                digi = Fixed(self.digital_base_image, digi_text, xysize=(self.width, self.d_height)) 
                #Create a render for our Fixed Box
                digi_render = renpy.render(digi, width, height, st, at)
                    
                # Create the render we will return.
                render = renpy.Render(self.width, self.d_height)

                # Blit (draw) the child's render to our render.
                render.blit(digi_render, (0,0))
                
            #Runs the realclock and autoclock functions checking to see if we are in those modes
            self.realclock()
            self.autoclock(st)

            #If we are in alarm_on mode, checks to see the alarm need to be rung
            if self.alarm_on == True:
                if self.last_minute != self.minutes:
                    self.play_alarm = False
                    self.last_minute = self.minutes
                self.start_alarm()
                    
            #This makes sure our object redraws itself after it makes changes
            renpy.redraw(self, 0)

            # Return the render.
            return render

        #Returns a list of all the child displayables for this displayable.
        def visit(self):
            return [self.base_image, self.hour_hand_image, self.minute_hand_image, self.second_hand_image, self.digital_base_image]

        #Returns the current hours, minutes, and seconds of the clock
        def get_time(self):
            h, m = divmod(self.minutes, 60)
            h = int(h)
            m = int(m)
            s = self.seconds%60
            s = int(s) #Can this be placed above?
            if h is 0:
                h = 12
            elif h > 12:
                h = h%12
            return h, m, s
            
        #Directly set the time of the clock
        def set_time(self, h=0, m=0):
            """
            h = hours
            m = minutes
            """
            self.seconds = ((h*60)+m)*60
            
        #Manually add time to the clock, with or without animation
        def add_time(self, h=0, m=0, animate=0): 
            """
            h = hours
            m = minutes
            animate = the number of seconds it takes for the time to be added
            """
            if self.realtime_run == False:
                num = ((h*60)+m)*60
                if animate:
                    self.step = num // float(animate*60)
                    self.seconds_target = self.seconds + num
                else:
                    self.seconds += num
        
        #Runs the clock mechanism automatically
        def autoclock(self, st):
            if self.auto_run:
                self.realtime_run = False
                if self.old_second is None:
                    dt = 0
                else:
                    dt = st - self.old_second
                self.old_second = st
                self.seconds += dt
                
        #Runs the clock based on the real world time        
        def realclock(self):
            if self.realtime_run:
                self.auto_run = False 
                t = datetime.today()
                self.seconds = (3600 * t.hour) + (60 * t.minute) + t.second
        
        #Sets the runmode of the clock, the second hand, and the sound
        def runmode(self, mode, snd=True):
            """
            mode= The mode of the clock: auto, real, or none (None turns off the clock) 
            snd= Turns on or off sound
            """
            if self.analogue:
                self.a_sound_on(snd, snd)
            else:
                self.alarm_on = snd
            if mode == "none":
                self.seconds_target = 0
                self.realtime_run = False
                self.auto_run = False
            else:
                if mode == "auto":
                    self.realtime_run = False
                    self.auto_run = True
                elif mode == "real":
                    self.auto_run = False
                    self.realtime_run = True
        
        #Sets the analogue sounds for the clock
        def a_sound_on(self, secOn, chOn):
            """
            secOn = Turns the second hand sound on or off
            chOn = Turns the chime sound on or off
            """
            if self.analogue:
                self.second_sound_on = secOn
                self.chime_on = chOn
                if self.second_sound_on:
                    if renpy.music.is_playing(channel='TockBG'):
                        renpy.music.stop(channel='TockBG', fadeout=0.1)
                    renpy.music.play("bgs/clock.mp3", channel='TockBG')
                else:
                    renpy.music.stop(channel='TockBG')
                if not self.chime_on:
                    renpy.music.stop(channel='ChimeBG')
        
        #Determines how many chimes should ring at any given hour and puts that audio queue together
        def chime_looper(self):
            h, m, s = self.get_time()
            ch = ["se/ChimePart.ogg",]*(h-1)
            ch.append("se/Chime1.ogg")
            return ch
        
        #Plays clock chimes on the hour
        def start_chime(self): 
            if self.chime_on:    
                if not self.play_chime:
                    if self.minutes%60 == 0:
                        self.play_chime = True
                        cf = self.chime_looper()
                        renpy.music.queue(cf, channel='ChimeBG')
        
        #Sets the alarm for the digital clock
        def set_alarm (self, h=0, m=0, on=False):
            self.alarm_on = on
            self.alarm_hr = h
            self.alarm_min = m
        
        #Plays the alarm when the time has arrived
        def start_alarm(self): 
            if self.alarm_on:    
                if not self.play_alarm:
                    h, m, s = self.get_time()
                    if self.alarm_hr == h and self.alarm_min == m:
                        self.play_alarm = True
                        if self.analogue:
                            renpy.music.play("se/BellAlarm.wav", channel='Alarm')
                        else:
                            renpy.music.play("se/alarm.wav", channel='Alarm')

                        







