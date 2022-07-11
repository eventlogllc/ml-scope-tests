import unittest
from unittest.mock import patch

@patch('si.nn')
@patch('si.ds')


class SI_test(unittest.TestCase):
  def test(MockNN, MockDS):
     si.nn()
     si.ds()
     
     out = StringIO.StringIO()
     err = StringIO.StringIO() 
     ### clear the stdout and stderr buffer
     out.flush()
     err.flush()
     with redirect_stdout(f) and redirect_stderr(f):
        output = out.getvalue()
        assert MockNN is si.nn
        assert MockDS is si.ds
        assert MockNN.called
        assert MockDS.called      

def main():
  suite = unittest.TestSuite()
  suite.addTest(SI_test('test'))
  unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == "__main__":
  unittest.main()

