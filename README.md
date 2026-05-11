**Halo**, 
repo ini dibuat sebagai bahan belajar automation menggunakan selenium. Di dalam repo ini berisi source code automation dengan beberapa metode seperti BDD dan Page Object Model, serta nanti nya akan berisi beberapa bahasa pemrograman seperti python dan javascript.

Berikut adalah penjelasan fungsi setiap folder dan alur kerja (workflow) dari framework automasi Anda:

1. Struktur Folder dan Fungsinya
a. features/: Tempat Anda menyimpan skenario pengujian (dengan ekstensi .feature) yang ditulis menggunakan format Gherkin (Given, When, Then). Bahasa ini mudah dibaca oleh manusia (non-teknis).
- features/steps/: Berisi file Python (seperti login_steps.py). File ini berfungsi menerjemahkan langkah-langkah bahasa Gherkin di feature file menjadi eksekusi kode Python yang sesungguhnya.
- environment.py: Digunakan untuk mengatur prasyarat (setup) dan pembersihan (teardown), contohnya: membuka browser (via WebDriver) sebelum skenario dimulai dan menutupnya setelah selesai (before_scenario dan after_scenario).
b. pages/: Berisi kelas-kelas Python yang mewakili halaman web (seperti login_page.py atau dashboard_page.py). Setiap class berisi methods (fungsi-fungsi) yang bisa dilakukan user di halaman tersebut, contoh: fungsi login(), get_username(), dll.
c. locators/: Berisi pendefinisian elemen web (seperti XPath, ID, CSS Selector) yang dipisahkan dari logika Pages. Contohnya: letak tombol login atau letak input username.
d. data/: Tempat menyimpan data-data pengujian secara terpisah, seperti file credentials.json. Ini memudahkan jika Anda ingin melakukan tes login dengan 10 akun berbeda tanpa mengubah kode program (Data-Driven Testing).
e. config/: Tempat menyimpan variabel global atau URL dasar aplikasi (seperti LOGIN_URL).


2. Alur Kerja (Workflow) Automasi
Ketika Anda menjalankan pengujian, inilah urutan alur kerja sistemnya:

a. Persiapan Browser (Environment): Selenium (melalui Behave) akan membaca file environment.py dan memicu before_scenario. WebDriver (seperti Google Chrome) akan terbuka dan dikonfigurasi.
b. Membaca Skenario (Features): Sistem membaca file .feature yang ingin dijalankan (contoh: User login successfully).
c. Memicu Langkah-Langkah Kode (Steps): Untuk setiap kalimat "Given, When, Then" di feature, sistem akan mencari fungsi yang sesuai (ter- mapping) di dalam folder features/steps/.
d. Mengambil Data (Data): Apabila step tersebut membutuhkan input (seperti username atau password), skrip di dalam file steps/ akan membaca file credentials.json yang ada di folder data/.
e. Menjalankan Aksi Halaman (Pages & Locators): File steps/ kemudian akan memanggil fungsi di dalam file pages/ (misalnya LoginPage). Kelas LoginPage ini akan melihat ke file locators/ untuk mengetahui posisi persis elemen web di browser, lalu menyuruh Selenium untuk melakukan aksi (seperti ketik password dan klik tombol).
f. Validasi/Pengecekan (Assertion): Pada langkah "Then", kode di steps/ akan kembali memanggil fungsi di pages/ untuk memeriksa apakah elemen berhasil muncul (misal: tulisan "Dashboard" muncul di halaman).
g. Penutup (Teardown): Setelah satu skenario tuntas, skrip di environment.py akan memicu after_scenario untuk menutup driver browser, lalu melanjutkannya ke skenario berikutnya.

Keuntungan Alur Kerja Ini: Jika suatu saat tim developer aplikasi mengubah posisi atau tampilan tombol Login, Anda hanya perlu mengubah locator-nya di folder locators/ tanpa perlu mengubah skenario feature atau kode steps yang jumlahnya banyak. Begitu pula bila Anda ingin menambahkan user untuk di-tes, cukup tambahkan datanya di data/credentials.json.