import unittest
import validators


from main import parse_date, hello, format_url


class MainTesting(unittest.TestCase):

    def test_hello(self):
        result = hello()
        assert result == "hello"

    def test_format_url(self):
        #test case 1: https://www.google.com
        #result: no change
        string = "https://www.google.com"
        target = "https://www.google.com"
        result = format_url(string)
        assert result == target
        assert(validators.url(result))

        #test case 2: https://google.com
        #result: no change
        string = "https://google.com"
        target = "https://google.com"
        result = format_url(string)
        assert result == target
        assert (validators.url(result))

        #test case 3: www.google.com
        #result: returns https://www.google.com
        string = "www.google.com"
        target = "https://www.google.com"
        result = format_url(string)
        assert result == target
        assert (validators.url(result))

        #test case 4: google.com
        #result: returns https://google.com
        string = "google.com"
        target = "https://google.com"
        result = format_url(string)
        assert (validators.url(result))

        #test_case_5: f.a.s.t
        #result: url validator will fail
        string = "f.a.s.t"
        target = "https://google.com"
        result = format_url(string)
        assert not (validators.url(result))

    def test_parse_date(self):
        pass
        #test case 1:


class CronTesting(unittest.TestCase):
    def test_delete_cron(self):
        pass

    def test_open_url(self):
        pass


if __name__ == '__main__':
    unittest.main()
