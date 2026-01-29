Feature: Navigasi

  Scenario: Membuka halaman Admin
    Given user berada di halaman dashboard
    When user klik navigasi admin
    Then user berhasil membuka halaman admin

  Scenario: Membuka halaman PIM
    Given user berada di halaman dashboard
    When user klik navigasi pim
    Then user berhasil membuka halaman admin

  Scenario: Membuka halaman Leave
    Given user berada di halaman dashboard
    When user klik navigasi leave
    Then user berhasil membuka halaman leave