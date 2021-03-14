import wx, datetime, time
from PBOPR import register

class RegisterController(register):
    def __init__(self,parent):
        register.__init__(self,parent)
    
    def m_button7OnButtonClick( self, event ):
        nama = self.input_nama.GetValue()
        nim = self.input_nim.GetValue()
        kelas = self.input_kelas.GetValue()
        prodi = self.input_prodi.GetValue()
        fakultas = self.input_fakultas.GetValue()
        angkatan = self.input_angkatan.GetValue()
        jenisKelamin = self.input_jenisKelamin.GetValue()
        tglLahir = self.input_tglLahir.GetValue()
        alamat = self.input_alamat.GetValue()

        print("HELLO WX!")
        print('Nama : ', nama)
        print('NIM : ', nim)
        print('Kelas : ', kelas)
        print('Program Studi : ', prodi)
        print('Fakultas : ', fakultas)
        print('Angkatan : ', angkatan)
        print('Jenis Kelamin : ', jenisKelamin)
        print('Tanggal Lahir : ', tglLahir)
        print('Alamat : ', alamat)


app = wx.App()
frame = RegisterController(parent=None)
frame.Show()
app.MainLoop()