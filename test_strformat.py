from strformat import print_formatted

def test_print_formatted(capsys):
    print_formatted(2)
    captured = capsys.readouterr()
    assert captured.out == '1 1 1 1\n2 2 2 10\n'
    
    print_formatted(5)
    captured = capsys.readouterr()
    assert captured.out == '1 1 1 1\n2 2 2 10\n3 3 3 11\n4 4 4 100\n5 5 5 101\n'
    
    print_formatted(0)
    captured = capsys.readouterr()
    assert captured.out == ''