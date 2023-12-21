from main import home_menu

def test_home_menu_option_1():
    result = home_menu()
    assert result == "1"