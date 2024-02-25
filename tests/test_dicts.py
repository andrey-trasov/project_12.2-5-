from utils.dicts import get_val


def test_get_val():
    assert get_val({"vcs": "mercurial"}, "vcs", "lol") == 'mercurial'
    assert get_val({"vcs": "mercurial"}, "abs", "lol") == "lol"
    assert get_val({"vcs": "mercurial"}, "abs") == 'git'