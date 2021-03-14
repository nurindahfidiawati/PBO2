# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.adv

###########################################################################
## Class register
###########################################################################

class register ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Register", pos = wx.DefaultPosition, size = wx.Size( 747,515 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL|wx.VSCROLL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_GRAYTEXT ) )

		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel3 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel3.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )

		fgSizer3 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer3.SetFlexibleDirection( wx.BOTH )
		fgSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText14 = wx.StaticText( self.m_panel3, wx.ID_ANY, u"HELLOOO WX .... !!!", wx.DefaultPosition, wx.Size( 1500,-1 ), wx.ALIGN_CENTER_HORIZONTAL )
		self.m_staticText14.Wrap( -1 )

		self.m_staticText14.SetFont( wx.Font( 30, wx.FONTFAMILY_TELETYPE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, True, wx.EmptyString ) )
		self.m_staticText14.SetBackgroundColour( wx.Colour( 45, 177, 206 ) )

		fgSizer3.Add( self.m_staticText14, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		fgSizer3.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText15 = wx.StaticText( self.m_panel3, wx.ID_ANY, u"Nama : Nur Indah Fidia Wati", wx.DefaultPosition, wx.Size( 1800,-1 ), wx.ALIGN_CENTER_HORIZONTAL )
		self.m_staticText15.Wrap( -1 )

		self.m_staticText15.SetFont( wx.Font( 20, wx.FONTFAMILY_TELETYPE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

		fgSizer3.Add( self.m_staticText15, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		fgSizer3.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText16 = wx.StaticText( self.m_panel3, wx.ID_ANY, u"NIM 192410101039", wx.DefaultPosition, wx.Size( 1800,-1 ), wx.ALIGN_CENTER_HORIZONTAL )
		self.m_staticText16.Wrap( -1 )

		self.m_staticText16.SetFont( wx.Font( 20, wx.FONTFAMILY_TELETYPE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, True, wx.EmptyString ) )
		self.m_staticText16.SetBackgroundColour( wx.Colour( 137, 211, 216 ) )

		fgSizer3.Add( self.m_staticText16, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		self.m_panel3.SetSizer( fgSizer3 )
		self.m_panel3.Layout()
		fgSizer3.Fit( self.m_panel3 )
		bSizer3.Add( self.m_panel3, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel11 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel11.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_SCROLLBAR ) )
		self.m_panel11.SetMinSize( wx.Size( -1,50 ) )

		fgSizer2 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		fgSizer2.SetMinSize( wx.Size( -1,20 ) )
		self.m_staticText81 = wx.StaticText( self.m_panel11, wx.ID_ANY, u"SELAMAT DATANG DI CODING WXPYTHON", wx.DefaultPosition, wx.Size( 1500,-1 ), wx.ALIGN_CENTER_HORIZONTAL )
		self.m_staticText81.Wrap( -1 )

		self.m_staticText81.SetFont( wx.Font( 17, wx.FONTFAMILY_TELETYPE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial Black" ) )
		self.m_staticText81.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )
		self.m_staticText81.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )

		fgSizer2.Add( self.m_staticText81, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		self.m_panel11.SetSizer( fgSizer2 )
		self.m_panel11.Layout()
		fgSizer2.Fit( self.m_panel11 )
		bSizer3.Add( self.m_panel11, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, u"Silahkan Isi Identitas Anda!", wx.DefaultPosition, wx.Size( 1500,-1 ), wx.ALIGN_CENTER_HORIZONTAL )
		self.m_staticText10.Wrap( -1 )

		self.m_staticText10.SetFont( wx.Font( 18, wx.FONTFAMILY_TELETYPE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.m_staticText10.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )
		self.m_staticText10.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )

		bSizer3.Add( self.m_staticText10, 0, wx.ALL, 5 )

		self.m_panel9 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel9.SetBackgroundColour( wx.Colour( 160, 225, 239 ) )
		self.m_panel9.SetMinSize( wx.Size( -1,800 ) )

		sbSizer2 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel9, wx.ID_ANY, wx.EmptyString ), wx.VERTICAL )

		fgSizer8 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer8.SetFlexibleDirection( wx.BOTH )
		fgSizer8.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText2 = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Nama", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )

		self.m_staticText2.SetFont( wx.Font( 14, wx.FONTFAMILY_TELETYPE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

		fgSizer8.Add( self.m_staticText2, 0, wx.ALL, 5 )

		self.input_nama = wx.TextCtrl( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), 0|wx.BORDER_RAISED )
		fgSizer8.Add( self.input_nama, 0, wx.ALL, 5 )

		self.m_staticText3 = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"NIM", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )

		self.m_staticText3.SetFont( wx.Font( 14, wx.FONTFAMILY_TELETYPE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

		fgSizer8.Add( self.m_staticText3, 0, wx.ALL, 5 )

		self.input_nim = wx.TextCtrl( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), 0|wx.BORDER_RAISED )
		fgSizer8.Add( self.input_nim, 0, wx.ALL, 5 )

		self.m_staticText4 = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Kelas", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )

		self.m_staticText4.SetFont( wx.Font( 14, wx.FONTFAMILY_TELETYPE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

		fgSizer8.Add( self.m_staticText4, 0, wx.ALL, 5 )

		self.input_kelas = wx.TextCtrl( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), 0|wx.BORDER_RAISED )
		fgSizer8.Add( self.input_kelas, 0, wx.ALL, 5 )

		self.m_staticText5 = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Program Studi", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )

		self.m_staticText5.SetFont( wx.Font( 14, wx.FONTFAMILY_TELETYPE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

		fgSizer8.Add( self.m_staticText5, 0, wx.ALL, 5 )

		self.input_prodi = wx.TextCtrl( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), 0|wx.BORDER_RAISED )
		fgSizer8.Add( self.input_prodi, 0, wx.ALL, 5 )

		self.m_staticText6 = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Fakultas", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )

		self.m_staticText6.SetFont( wx.Font( 14, wx.FONTFAMILY_TELETYPE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

		fgSizer8.Add( self.m_staticText6, 0, wx.ALL, 5 )

		self.input_fakultas = wx.TextCtrl( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), 0|wx.BORDER_RAISED )
		fgSizer8.Add( self.input_fakultas, 0, wx.ALL, 5 )

		self.m_staticText7 = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Angkatan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )

		self.m_staticText7.SetFont( wx.Font( 14, wx.FONTFAMILY_TELETYPE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

		fgSizer8.Add( self.m_staticText7, 0, wx.ALL, 5 )

		self.input_angkatan = wx.SpinCtrl( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), wx.SP_ARROW_KEYS|wx.BORDER_RAISED, 0, 10, 0 )
		fgSizer8.Add( self.input_angkatan, 0, wx.ALL, 5 )

		self.m_staticText8 = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Jenis Kelamin", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )

		self.m_staticText8.SetFont( wx.Font( 14, wx.FONTFAMILY_TELETYPE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

		fgSizer8.Add( self.m_staticText8, 0, wx.ALL, 5 )

		input_jenisKelaminChoices = [ u"Laki-Laki", u"Perempuan" ]
		self.input_jenisKelamin = wx.ComboBox( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Perempuan", wx.DefaultPosition, wx.Size( 200,-1 ), input_jenisKelaminChoices, 0|wx.BORDER_RAISED )
		self.input_jenisKelamin.SetSelection( 1 )
		fgSizer8.Add( self.input_jenisKelamin, 0, wx.ALL, 5 )

		self.m_staticText11 = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Tanggal Lahir", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )

		self.m_staticText11.SetFont( wx.Font( 14, wx.FONTFAMILY_TELETYPE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

		fgSizer8.Add( self.m_staticText11, 0, wx.ALL, 5 )

		self.input_tglLahir = wx.adv.DatePickerCtrl( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.Size( 200,-1 ), wx.adv.DP_DEFAULT|wx.BORDER_RAISED )
		fgSizer8.Add( self.input_tglLahir, 0, wx.ALL, 5 )

		self.m_staticText12 = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Alamat", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )

		self.m_staticText12.SetFont( wx.Font( 14, wx.FONTFAMILY_TELETYPE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

		fgSizer8.Add( self.m_staticText12, 0, wx.ALL, 5 )

		self.input_alamat = wx.TextCtrl( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), 0|wx.BORDER_RAISED )
		fgSizer8.Add( self.input_alamat, 0, wx.ALL, 5 )


		fgSizer8.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_button7 = wx.Button( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Daftar", wx.DefaultPosition, wx.Size( 200,-1 ), 0|wx.BORDER_RAISED )

		self.m_button7.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_FILE_SAVE, wx.ART_OTHER ) )
		self.m_button7.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )

		fgSizer8.Add( self.m_button7, 0, wx.ALL, 5 )


		sbSizer2.Add( fgSizer8, 1, wx.EXPAND, 5 )


		self.m_panel9.SetSizer( sbSizer2 )
		self.m_panel9.Layout()
		sbSizer2.Fit( self.m_panel9 )
		bSizer3.Add( self.m_panel9, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer3 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button7.Bind( wx.EVT_BUTTON, self.m_button7OnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def m_button7OnButtonClick( self, event ):
		event.Skip()


