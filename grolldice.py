#!/usr/bin/env python
# -*- coding: utf-8 -*-
# generated by wxGlade 0.6.3 on Sun Nov 22 16:00:21 2009

import wx
import random,os

# begin wxGlade: extracode
# end wxGlade

class dice(object):
    def __init__( self, side =0 , addsub = 0,  roll = True ):
        self.side = max( side , 0)
        self.addsub = addsub
        self.result = 0
        if roll :
            self.roll()
    def roll(self):
        if self.side > 0 :
            self.result = random.randint( 1, self.side ) + self.addsub 
        else :
            self.result =  self.addsub 
        return self
    def __str__(self):
        return "%d=%s" % ( self.result, self.getinfostr())
    def getinfostr(self):
        ad , sd = '' , ''
        if self.addsub :
            ad = "%+d" % self.addsub
        if self.side :
            sd = "d%d" %   self.side
        return sd + ad
    def copy( self, roll = True ):
        return dice( self.side, self.addsub , roll )
    def challenge( self , targetdc, critcal = [ 20] ):
        """ fail:0 success:1 critcal:2"""
        rollval = self.result - self.addsub
        ishit =self.result >= targetdc
        if ( ishit or rollval == 20) and rollval in critcal :
            crirol = self.copy(True) 
            return 2 if crirol.challenge( targetdc , []) else 1
        else:
            return 1 if ishit and rollval != 1 else 0

class diceset(object):
    def __init__( self ):
        self.sets = []
    def append(self,other, count = 1):
        if isinstance(other, dice) :
            for i in range(count) :
                self.sets.append(other.copy())
        else :
            pass
        return self
    def pop(self):
         return self.sets.pop()
    def roll(self):
        for a in self.sets:
            a.roll()
        return self
    def getsum(self):
        return sum( [ a.result for a in self.sets ] )
    def copy(self):
        rtn = diceset()
        for a in self.sets:
            rtn.append( a)
        return rtn
    def __str__(self):
        rtn = '+'.join( [ a.getinfostr() for a in self.sets ] )
        return "%s" % ( rtn )
    def getRollStr(self):
        self.roll()
        dsum = self.getsum()
        sdsum = '+'.join( [ str(a.result) for a in self.sets ] )
        return "%s(%s)" % ( dsum , sdsum )

class WxRollDiceFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: WxRollDiceFrame.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        basedirname = os.path.dirname(os.path.abspath(__file__))
        self.bitmap_button_2 = wx.BitmapButton(self, 4, wx.Bitmap(os.path.join( basedirname, "d4_128x128.png"), wx.BITMAP_TYPE_ANY))
        self.bitmap_button_3 = wx.BitmapButton(self, 6, wx.Bitmap(os.path.join( basedirname, "d6_128x128.png"), wx.BITMAP_TYPE_ANY))
        self.bitmap_button_4 = wx.BitmapButton(self, 8, wx.Bitmap(os.path.join( basedirname, "d8_128x128.png"), wx.BITMAP_TYPE_ANY))
        self.bitmap_button_5 = wx.BitmapButton(self, 10, wx.Bitmap(os.path.join( basedirname, "d10_128x128.png"), wx.BITMAP_TYPE_ANY))
        self.bitmap_button_6 = wx.BitmapButton(self, 12, wx.Bitmap(os.path.join( basedirname, "d12_128x128.png"), wx.BITMAP_TYPE_ANY))
        self.bitmap_button_7 = wx.BitmapButton(self, 20, wx.Bitmap(os.path.join( basedirname, "d20_128x128.png"), wx.BITMAP_TYPE_ANY))
        self.bitmap_button_8 = wx.BitmapButton(self, 100, wx.Bitmap(os.path.join( basedirname, "d100_128x128.png"), wx.BITMAP_TYPE_ANY))
        self.button_Roll = wx.Button(self, -1, "Roll")
        self.spin_ctrl_1 = wx.SpinCtrl(self, -1, "1", min=1, max=100, style=wx.SP_ARROW_KEYS|wx.SP_WRAP|wx.TE_AUTO_URL|wx.TE_NOHIDESEL)
        self.button_add1 = wx.Button(self, -1, "+1")
        self.button_sub1 = wx.Button(self, -1, "-1")
        self.button_BS = wx.Button(self, -1, "BS")
        self.button_reset = wx.Button(self, -1, "Reset")
        self.label_result = wx.StaticText(self, -1, "0", style=wx.ALIGN_CENTRE)
        self.text_ctrl_1 = wx.TextCtrl(self, -1, "")
        self.list_ctrl_1 = wx.ListCtrl(self, -1, style=wx.LC_REPORT|wx.SUNKEN_BORDER)

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_BUTTON, self.evt_dice_in, id=4)
        self.Bind(wx.EVT_BUTTON, self.evt_dice_in, id=6)
        self.Bind(wx.EVT_BUTTON, self.evt_dice_in, id=8)
        self.Bind(wx.EVT_BUTTON, self.evt_dice_in, id=10)
        self.Bind(wx.EVT_BUTTON, self.evt_dice_in, id=12)
        self.Bind(wx.EVT_BUTTON, self.evt_dice_in, id=20)
        self.Bind(wx.EVT_BUTTON, self.evt_dice_in, id=100)
        self.Bind(wx.EVT_BUTTON, self.evt_roll, self.button_Roll)
        self.Bind(wx.EVT_BUTTON, self.evt_add1, self.button_add1)
        self.Bind(wx.EVT_BUTTON, self.evt_sub1, self.button_sub1)
        self.Bind(wx.EVT_BUTTON, self.evt_bs, self.button_BS)
        self.Bind(wx.EVT_BUTTON, self.evt_reset, self.button_reset)
        # end wxGlade

        self.currentdiceset = diceset()
        self.updatedices()
        self.list_ctrl_1.InsertColumn(0, '', format=wx.LIST_FORMAT_LEFT, width=1024)

    def __set_properties(self):
        # begin wxGlade: WxRollDiceFrame.__set_properties
        self.SetTitle("WxDiceRoll")
        self.SetSize((984, 964))
        self.bitmap_button_2.SetSize(self.bitmap_button_2.GetBestSize())
        self.bitmap_button_3.SetSize(self.bitmap_button_3.GetBestSize())
        self.bitmap_button_4.SetSize(self.bitmap_button_4.GetBestSize())
        self.bitmap_button_5.SetSize(self.bitmap_button_5.GetBestSize())
        self.bitmap_button_6.SetSize(self.bitmap_button_6.GetBestSize())
        self.bitmap_button_7.SetSize(self.bitmap_button_7.GetBestSize())
        self.bitmap_button_8.SetSize(self.bitmap_button_8.GetBestSize())
        self.button_Roll.SetFont(wx.Font(24, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Sans"))
        self.spin_ctrl_1.SetFont(wx.Font(24, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        self.button_add1.SetFont(wx.Font(16, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Sans"))
        self.button_sub1.SetFont(wx.Font(16, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Sans"))
        self.button_BS.SetFont(wx.Font(16, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Sans"))
        self.button_reset.SetFont(wx.Font(16, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Sans"))
        self.label_result.SetFont(wx.Font(48, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        self.list_ctrl_1.SetMinSize((100, 80))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: WxRollDiceFrame.__do_layout
        sizer_2 = wx.BoxSizer(wx.VERTICAL)
        sizer_3 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_5 = wx.BoxSizer(wx.VERTICAL)
        sizer_4 = wx.BoxSizer(wx.VERTICAL)
        sizer_1 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_1.Add(self.bitmap_button_2, 0, 0, 0)
        sizer_1.Add(self.bitmap_button_3, 0, 0, 0)
        sizer_1.Add(self.bitmap_button_4, 0, 0, 0)
        sizer_1.Add(self.bitmap_button_5, 0, 0, 0)
        sizer_1.Add(self.bitmap_button_6, 0, 0, 0)
        sizer_1.Add(self.bitmap_button_7, 0, 0, 0)
        sizer_1.Add(self.bitmap_button_8, 0, 0, 0)
        sizer_2.Add(sizer_1, 0, wx.EXPAND, 0)
        sizer_4.Add(self.button_Roll, 2, wx.EXPAND, 0)
        sizer_4.Add(self.spin_ctrl_1, 1, wx.EXPAND, 0)
        sizer_4.Add(self.button_add1, 1, wx.EXPAND, 0)
        sizer_4.Add(self.button_sub1, 1, wx.EXPAND, 0)
        sizer_4.Add(self.button_BS, 1, wx.EXPAND, 0)
        sizer_4.Add(self.button_reset, 1, wx.EXPAND, 0)
        sizer_3.Add(sizer_4, 1, wx.EXPAND, 0)
        sizer_5.Add(self.label_result, 0, wx.EXPAND, 0)
        sizer_5.Add(self.text_ctrl_1, 0, wx.EXPAND, 0)
        sizer_5.Add(self.list_ctrl_1, 1, wx.EXPAND, 0)
        sizer_3.Add(sizer_5, 3, wx.EXPAND, 0)
        sizer_2.Add(sizer_3, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_2)
        self.Layout()
        # end wxGlade
    def updatedices(self):
        self.text_ctrl_1.ChangeValue( str(self.currentdiceset) ) 

    def evt_add1(self, event): # wxGlade: WxRollDiceFrame.<event_handler>
        self.currentdiceset.append( dice(0,self.spin_ctrl_1.GetValue()) )
        self.updatedices()

    def evt_sub1(self, event): # wxGlade: WxRollDiceFrame.<event_handler>
        self.currentdiceset.append( dice(0,-1*self.spin_ctrl_1.GetValue()) )
        self.updatedices()

    def evt_bs(self, event): # wxGlade: WxRollDiceFrame.<event_handler>
        self.currentdiceset.pop()
        self.updatedices()

    def evt_reset(self, event): # wxGlade: WxRollDiceFrame.<event_handler>
        self.currentdiceset = diceset()
        self.updatedices()

    def evt_roll(self, event): # wxGlade: WxRollDiceFrame.<event_handler>
        rollstr = self.currentdiceset.getRollStr()
        printstr = "%s = %s" % ( rollstr ,  self.currentdiceset) 
        self.list_ctrl_1.InsertStringItem(0,printstr)
        self.label_result.SetLabel( rollstr)
    def evt_dice_n(self, event): # wxGlade: WxRollDiceFrame.<event_handler>
        self.currentdiceset.append( dice(event.GetId() ),self.spin_ctrl_1.GetValue())
        self.updatedices()

    def evt_dice_in(self, event): # wxGlade: WxRollDiceFrame.<event_handler>
        self.currentdiceset.append( dice(event.GetId() ),self.spin_ctrl_1.GetValue())
        self.updatedices()

# end of class WxRollDiceFrame

class grolldiceapp(wx.PySimpleApp):
    """
    """

if __name__ == "__main__":
    app = grolldiceapp(0)
    wx.InitAllImageHandlers()
    frame_1 = WxRollDiceFrame(None, -1, "")
    app.SetTopWindow(frame_1)
    frame_1.Show()
    app.MainLoop()
