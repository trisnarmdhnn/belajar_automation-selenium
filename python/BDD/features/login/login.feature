Feature: Login OrangeHRM

  Scenario: Login sukses
    Given user membuka halaman login
    When user login dengan username "Admin" dan password "admin123"
    Then user berhasil masuk ke dashboard

  Scenario: Login gagal - password salah
    Given user membuka halaman login
    When user login dengan username "Admin" dan password "admin"
    Then muncul pesan error "Invalid credentials"

  Scenario: Login gagal - username kosong
    Given user membuka halaman login
    When user login dengan password "admin"
    Then muncul pesan error field "Required"

  Scenario: Login gagal - password kosong
    Given user membuka halaman login
    When user login dengan username "Admin"
    Then muncul pesan error field "Required"
