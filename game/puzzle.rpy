# klondike.rpy - Klondike Solitaire
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

init python: #################################################################퍼즐 1
    class puzzle1(object):
        def __init__(self):
            # Constants that let us easily change where the game is
            # located.
            LEFT=340
            TOP=160
            COL_SPACING = 200
            ROW_SPACING = 200
            self.COL_NUM = 4
            self.ROW_NUM = 3
            # Create the table, stock, and waste.
            self.table = t = Table(base="puzzles/base.png", back="puzzles/base.png")
            rotate_random = [0,0,0,90,180,270]
            deck = []
            # Create the stock and shuffle it.
            for i in range(0, self.COL_NUM):
                for j in range(0, self.ROW_NUM):
                    value = (i, j)
                    t.card(value, "puzzles/puz1/puz1-%d-%d.png" % (i,j))
                    t.set_faceup(value, True)
                    t.set_rotate(value, renpy.random.choice(rotate_random))
                    deck.append(value)
            renpy.random.shuffle(deck)
            # The 12 card spots.
            self.foundations = [ ]
            for i in range(0, self.COL_NUM):
                for j in range(0, self.ROW_NUM):
                    s = t.stack(LEFT + COL_SPACING * i, TOP + ROW_SPACING * j, xoff=0, yoff=0, drag=DRAG_TOP, drop=True, click=True)
                    self.foundations.append(s)
                    s.append(deck.pop())
        def show(self):
            self.table.show()
        def hide(self):
            self.table.hide()
        def foundation_drag(self, evt):
            # We can only drag one card at a time to a foundation.
            if len(evt.drag_cards) != 1:
                return False
            orig_s = evt.stack
            target_s = evt.drop_stack
            # Get the "top" card
            orig_c = evt.drag_cards[0]
            target_c = evt.drop_stack[-1]
            # swtich places
            target_s.append(orig_c)
            orig_s.append(target_c)
            renpy.sound.play("se/book_page.ogg", channel=1)
            return "foundation_drag"
        def card_click(self, evt):
            orig_s = evt.stack
            # If they clicked on a stack, then rotate the "top" card
            # (There should only be one card)
            if orig_s:
                orig_c = orig_s[-1]
                self.table.set_rotate(orig_c, self.table.get_rotate(orig_c) + 90)
                renpy.sound.play("se/flip_card.wav", channel=2)
            return "card_click %d" % self.table.get_rotate(orig_c)
        def interact(self):
            evt = ui.interact()
            rv = False
            # Check the various events, and dispatch them to the methods
            # that handle them.
            if evt.type == "drag":
                if evt.drop_stack in self.foundations:
                    rv = self.foundation_drag(evt)
            elif evt.type == "click":
                rv = self.card_click(evt)
            # Check to see that the correct peice is in the correct spot
            # if I had of been clever, I would have made the foundations
            # a two dimentional array
            for i in range(0, self.COL_NUM):
                for j in range(0, self.ROW_NUM):
                    f = self.foundations[j + (i*self.ROW_NUM)]
                    ii, jj =  f[0] # the value of the card 
                    # is it upright?
                    if (self.table.get_rotate(f[0]) % 360 != 0):
                        return rv
                    # is it in the right place?
                    if ii != i or jj != j:
                        return rv
            # if it makes it to here all the peices were upright and in the correct place
            return "win"
        # Sets things as sensitive (or not).
        def set_sensitive(self, value):
            self.table.set_sensitive(value)
#############################################################################

init python: #################################################################퍼즐 2
    class puzzle2(object):
        def __init__(self):
            # Constants that let us easily change where the game is
            # located.
            LEFT=340
            TOP=160
            COL_SPACING = 200
            ROW_SPACING = 200
            self.COL_NUM = 4
            self.ROW_NUM = 3
            # Create the table, stock, and waste.
            self.table = t = Table(base="puzzles/base.png", back="puzzles/base.png")
            rotate_random = [0,0,0,90,180,270]
            deck = []
            # Create the stock and shuffle it.
            for i in range(0, self.COL_NUM):
                for j in range(0, self.ROW_NUM):
                    value = (i, j)
                    t.card(value, "puzzles/puz2/puz2-%d-%d.png" % (i,j))
                    t.set_faceup(value, True)
                    t.set_rotate(value, renpy.random.choice(rotate_random))
                    deck.append(value)
            renpy.random.shuffle(deck)
            # The 12 card spots.
            self.foundations = [ ]
            for i in range(0, self.COL_NUM):
                for j in range(0, self.ROW_NUM):
                    s = t.stack(LEFT + COL_SPACING * i, TOP + ROW_SPACING * j, xoff=0, yoff=0, drag=DRAG_TOP, drop=True, click=True)
                    self.foundations.append(s)
                    s.append(deck.pop())
        def show(self):
            self.table.show()
        def hide(self):
            self.table.hide()
        def foundation_drag(self, evt):
            # We can only drag one card at a time to a foundation.
            if len(evt.drag_cards) != 1:
                return False
            orig_s = evt.stack
            target_s = evt.drop_stack
            # Get the "top" card
            orig_c = evt.drag_cards[0]
            target_c = evt.drop_stack[-1]
            # swtich places
            target_s.append(orig_c)
            orig_s.append(target_c)
            renpy.sound.play("se/book_page.ogg", channel=1)
            return "foundation_drag"
        def card_click(self, evt):
            orig_s = evt.stack
            # If they clicked on a stack, then rotate the "top" card
            # (There should only be one card)
            if orig_s:
                orig_c = orig_s[-1]
                self.table.set_rotate(orig_c, self.table.get_rotate(orig_c) + 90)
                renpy.sound.play("se/flip_card.wav", channel=2)
            return "card_click %d" % self.table.get_rotate(orig_c)
        def interact(self):
            evt = ui.interact()
            rv = False
            # Check the various events, and dispatch them to the methods
            # that handle them.
            if evt.type == "drag":
                if evt.drop_stack in self.foundations:
                    rv = self.foundation_drag(evt)
            elif evt.type == "click":
                rv = self.card_click(evt)
            # Check to see that the correct peice is in the correct spot
            # if I had of been clever, I would have made the foundations
            # a two dimentional array
            for i in range(0, self.COL_NUM):
                for j in range(0, self.ROW_NUM):
                    f = self.foundations[j + (i*self.ROW_NUM)]
                    ii, jj =  f[0] # the value of the card 
                    # is it upright?
                    if (self.table.get_rotate(f[0]) % 360 != 0):
                        return rv
                    # is it in the right place?
                    if ii != i or jj != j:
                        return rv
            # if it makes it to here all the peices were upright and in the correct place
            return "win"
        # Sets things as sensitive (or not).
        def set_sensitive(self, value):
            self.table.set_sensitive(value)
#############################################################################

init python: #################################################################퍼즐 3
    class puzzle3(object):
        def __init__(self):
            # Constants that let us easily change where the game is
            # located.
            LEFT=340
            TOP=160
            COL_SPACING = 200
            ROW_SPACING = 200
            self.COL_NUM = 4
            self.ROW_NUM = 3
            # Create the table, stock, and waste.
            self.table = t = Table(base="puzzles/base.png", back="puzzles/base.png")
            rotate_random = [0,0,0,90,180,270]
            deck = []
            # Create the stock and shuffle it.
            for i in range(0, self.COL_NUM):
                for j in range(0, self.ROW_NUM):
                    value = (i, j)
                    t.card(value, "puzzles/puz3/puz3-%d-%d.png" % (i,j))
                    t.set_faceup(value, True)
                    t.set_rotate(value, renpy.random.choice(rotate_random))
                    deck.append(value)
            renpy.random.shuffle(deck)
            # The 12 card spots.
            self.foundations = [ ]
            for i in range(0, self.COL_NUM):
                for j in range(0, self.ROW_NUM):
                    s = t.stack(LEFT + COL_SPACING * i, TOP + ROW_SPACING * j, xoff=0, yoff=0, drag=DRAG_TOP, drop=True, click=True)
                    self.foundations.append(s)
                    s.append(deck.pop())
        def show(self):
            self.table.show()
        def hide(self):
            self.table.hide()
        def foundation_drag(self, evt):
            # We can only drag one card at a time to a foundation.
            if len(evt.drag_cards) != 1:
                return False
            orig_s = evt.stack
            target_s = evt.drop_stack
            # Get the "top" card
            orig_c = evt.drag_cards[0]
            target_c = evt.drop_stack[-1]
            # swtich places
            target_s.append(orig_c)
            orig_s.append(target_c)
            renpy.sound.play("se/book_page.ogg", channel=1)
            return "foundation_drag"
        def card_click(self, evt):
            orig_s = evt.stack
            # If they clicked on a stack, then rotate the "top" card
            # (There should only be one card)
            if orig_s:
                orig_c = orig_s[-1]
                self.table.set_rotate(orig_c, self.table.get_rotate(orig_c) + 90)
                renpy.sound.play("se/flip_card.wav", channel=2)
            return "card_click %d" % self.table.get_rotate(orig_c)
        def interact(self):
            evt = ui.interact()
            rv = False
            # Check the various events, and dispatch them to the methods
            # that handle them.
            if evt.type == "drag":
                if evt.drop_stack in self.foundations:
                    rv = self.foundation_drag(evt)
            elif evt.type == "click":
                rv = self.card_click(evt)
            # Check to see that the correct peice is in the correct spot
            # if I had of been clever, I would have made the foundations
            # a two dimentional array
            for i in range(0, self.COL_NUM):
                for j in range(0, self.ROW_NUM):
                    f = self.foundations[j + (i*self.ROW_NUM)]
                    ii, jj =  f[0] # the value of the card 
                    # is it upright?
                    if (self.table.get_rotate(f[0]) % 360 != 0):
                        return rv
                    # is it in the right place?
                    if ii != i or jj != j:
                        return rv
            # if it makes it to here all the peices were upright and in the correct place
            return "win"
        # Sets things as sensitive (or not).
        def set_sensitive(self, value):
            self.table.set_sensitive(value)
#############################################################################

init python: #################################################################퍼즐 4
    class puzzle4(object):
        def __init__(self):
            # Constants that let us easily change where the game is
            # located.
            LEFT=340
            TOP=160
            COL_SPACING = 200
            ROW_SPACING = 200
            self.COL_NUM = 4
            self.ROW_NUM = 3
            # Create the table, stock, and waste.
            self.table = t = Table(base="puzzles/base.png", back="puzzles/base.png")
            rotate_random = [0,0,0,90,180,270]
            deck = []
            # Create the stock and shuffle it.
            for i in range(0, self.COL_NUM):
                for j in range(0, self.ROW_NUM):
                    value = (i, j)
                    t.card(value, "puzzles/puz4/puz4-%d-%d.png" % (i,j))
                    t.set_faceup(value, True)
                    t.set_rotate(value, renpy.random.choice(rotate_random))
                    deck.append(value)
            renpy.random.shuffle(deck)
            # The 12 card spots.
            self.foundations = [ ]
            for i in range(0, self.COL_NUM):
                for j in range(0, self.ROW_NUM):
                    s = t.stack(LEFT + COL_SPACING * i, TOP + ROW_SPACING * j, xoff=0, yoff=0, drag=DRAG_TOP, drop=True, click=True)
                    self.foundations.append(s)
                    s.append(deck.pop())
        def show(self):
            self.table.show()
        def hide(self):
            self.table.hide()
        def foundation_drag(self, evt):
            # We can only drag one card at a time to a foundation.
            if len(evt.drag_cards) != 1:
                return False
            orig_s = evt.stack
            target_s = evt.drop_stack
            # Get the "top" card
            orig_c = evt.drag_cards[0]
            target_c = evt.drop_stack[-1]
            # swtich places
            target_s.append(orig_c)
            orig_s.append(target_c)
            renpy.sound.play("se/book_page.ogg", channel=1)
            return "foundation_drag"
        def card_click(self, evt):
            orig_s = evt.stack
            # If they clicked on a stack, then rotate the "top" card
            # (There should only be one card)
            if orig_s:
                orig_c = orig_s[-1]
                self.table.set_rotate(orig_c, self.table.get_rotate(orig_c) + 90)
                renpy.sound.play("se/flip_card.wav", channel=2)
            return "card_click %d" % self.table.get_rotate(orig_c)
        def interact(self):
            evt = ui.interact()
            rv = False
            # Check the various events, and dispatch them to the methods
            # that handle them.
            if evt.type == "drag":
                if evt.drop_stack in self.foundations:
                    rv = self.foundation_drag(evt)
            elif evt.type == "click":
                rv = self.card_click(evt)
            # Check to see that the correct peice is in the correct spot
            # if I had of been clever, I would have made the foundations
            # a two dimentional array
            for i in range(0, self.COL_NUM):
                for j in range(0, self.ROW_NUM):
                    f = self.foundations[j + (i*self.ROW_NUM)]
                    ii, jj =  f[0] # the value of the card 
                    # is it upright?
                    if (self.table.get_rotate(f[0]) % 360 != 0):
                        return rv
                    # is it in the right place?
                    if ii != i or jj != j:
                        return rv
            # if it makes it to here all the peices were upright and in the correct place
            return "win"
        # Sets things as sensitive (or not).
        def set_sensitive(self, value):
            self.table.set_sensitive(value)
#############################################################################

init python: #################################################################퍼즐 5
    class puzzle5(object):
        def __init__(self):
            # Constants that let us easily change where the game is
            # located.
            LEFT=340
            TOP=160
            COL_SPACING = 200
            ROW_SPACING = 200
            self.COL_NUM = 4
            self.ROW_NUM = 3
            # Create the table, stock, and waste.
            self.table = t = Table(base="puzzles/base.png", back="puzzles/base.png")
            rotate_random = [0,0,0,90,180,270]
            deck = []
            # Create the stock and shuffle it.
            for i in range(0, self.COL_NUM):
                for j in range(0, self.ROW_NUM):
                    value = (i, j)
                    t.card(value, "puzzles/puz5/puz5-%d-%d.png" % (i,j))
                    t.set_faceup(value, True)
                    t.set_rotate(value, renpy.random.choice(rotate_random))
                    deck.append(value)
            renpy.random.shuffle(deck)
            # The 12 card spots.
            self.foundations = [ ]
            for i in range(0, self.COL_NUM):
                for j in range(0, self.ROW_NUM):
                    s = t.stack(LEFT + COL_SPACING * i, TOP + ROW_SPACING * j, xoff=0, yoff=0, drag=DRAG_TOP, drop=True, click=True)
                    self.foundations.append(s)
                    s.append(deck.pop())
        def show(self):
            self.table.show()
        def hide(self):
            self.table.hide()
        def foundation_drag(self, evt):
            # We can only drag one card at a time to a foundation.
            if len(evt.drag_cards) != 1:
                return False
            orig_s = evt.stack
            target_s = evt.drop_stack
            # Get the "top" card
            orig_c = evt.drag_cards[0]
            target_c = evt.drop_stack[-1]
            # swtich places
            target_s.append(orig_c)
            orig_s.append(target_c)
            renpy.sound.play("se/book_page.ogg", channel=1)
            return "foundation_drag"
        def card_click(self, evt):
            orig_s = evt.stack
            # If they clicked on a stack, then rotate the "top" card
            # (There should only be one card)
            if orig_s:
                orig_c = orig_s[-1]
                self.table.set_rotate(orig_c, self.table.get_rotate(orig_c) + 90)
                renpy.sound.play("se/flip_card.wav", channel=2)
            return "card_click %d" % self.table.get_rotate(orig_c)
        def interact(self):
            evt = ui.interact()
            rv = False
            # Check the various events, and dispatch them to the methods
            # that handle them.
            if evt.type == "drag":
                if evt.drop_stack in self.foundations:
                    rv = self.foundation_drag(evt)
            elif evt.type == "click":
                rv = self.card_click(evt)
            # Check to see that the correct peice is in the correct spot
            # if I had of been clever, I would have made the foundations
            # a two dimentional array
            for i in range(0, self.COL_NUM):
                for j in range(0, self.ROW_NUM):
                    f = self.foundations[j + (i*self.ROW_NUM)]
                    ii, jj =  f[0] # the value of the card 
                    # is it upright?
                    if (self.table.get_rotate(f[0]) % 360 != 0):
                        return rv
                    # is it in the right place?
                    if ii != i or jj != j:
                        return rv
            # if it makes it to here all the peices were upright and in the correct place
            return "win"
        # Sets things as sensitive (or not).
        def set_sensitive(self, value):
            self.table.set_sensitive(value)
#############################################################################

init python: #################################################################퍼즐 6
    class puzzle6(object):
        def __init__(self):
            # Constants that let us easily change where the game is
            # located.
            LEFT=340
            TOP=160
            COL_SPACING = 200
            ROW_SPACING = 200
            self.COL_NUM = 4
            self.ROW_NUM = 3
            # Create the table, stock, and waste.
            self.table = t = Table(base="puzzles/base.png", back="puzzles/base.png")
            rotate_random = [0,0,0,90,180,270]
            deck = []
            # Create the stock and shuffle it.
            for i in range(0, self.COL_NUM):
                for j in range(0, self.ROW_NUM):
                    value = (i, j)
                    t.card(value, "puzzles/puz6/puz6-%d-%d.png" % (i,j))
                    t.set_faceup(value, True)
                    t.set_rotate(value, renpy.random.choice(rotate_random))
                    deck.append(value)
            renpy.random.shuffle(deck)
            # The 12 card spots.
            self.foundations = [ ]
            for i in range(0, self.COL_NUM):
                for j in range(0, self.ROW_NUM):
                    s = t.stack(LEFT + COL_SPACING * i, TOP + ROW_SPACING * j, xoff=0, yoff=0, drag=DRAG_TOP, drop=True, click=True)
                    self.foundations.append(s)
                    s.append(deck.pop())
        def show(self):
            self.table.show()
        def hide(self):
            self.table.hide()
        def foundation_drag(self, evt):
            # We can only drag one card at a time to a foundation.
            if len(evt.drag_cards) != 1:
                return False
            orig_s = evt.stack
            target_s = evt.drop_stack
            # Get the "top" card
            orig_c = evt.drag_cards[0]
            target_c = evt.drop_stack[-1]
            # swtich places
            target_s.append(orig_c)
            orig_s.append(target_c)
            renpy.sound.play("se/book_page.ogg", channel=1)
            return "foundation_drag"
        def card_click(self, evt):
            orig_s = evt.stack
            # If they clicked on a stack, then rotate the "top" card
            # (There should only be one card)
            if orig_s:
                orig_c = orig_s[-1]
                self.table.set_rotate(orig_c, self.table.get_rotate(orig_c) + 90)
                renpy.sound.play("se/flip_card.wav", channel=2)
            return "card_click %d" % self.table.get_rotate(orig_c)
        def interact(self):
            evt = ui.interact()
            rv = False
            # Check the various events, and dispatch them to the methods
            # that handle them.
            if evt.type == "drag":
                if evt.drop_stack in self.foundations:
                    rv = self.foundation_drag(evt)
            elif evt.type == "click":
                rv = self.card_click(evt)
            # Check to see that the correct peice is in the correct spot
            # if I had of been clever, I would have made the foundations
            # a two dimentional array
            for i in range(0, self.COL_NUM):
                for j in range(0, self.ROW_NUM):
                    f = self.foundations[j + (i*self.ROW_NUM)]
                    ii, jj =  f[0] # the value of the card 
                    # is it upright?
                    if (self.table.get_rotate(f[0]) % 360 != 0):
                        return rv
                    # is it in the right place?
                    if ii != i or jj != j:
                        return rv
            # if it makes it to here all the peices were upright and in the correct place
            return "win"
        # Sets things as sensitive (or not).
        def set_sensitive(self, value):
            self.table.set_sensitive(value)
#############################################################################




