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
        
  def test_side_effect(MockNN, MockDS):
     si.nn()
     si.ds()
     
     out = StringIO.StringIO()
     err = StringIO.StringIO() 
     ### 
     def _func_get_data_side_effect(url, offset):
        if offset == 1:
           return { 2, 3 }
        else:
           return { -2, -3 }
          
     def _func_randome_side_effect(nodes, offset):
        if offset == 1:
           return nodes[0:1]
        else:
           return nodes[2:3]
          
     ### clear the stdout and stderr buffer
     out.flush()
     err.flush()
     with redirect_stdout(f) and redirect_stderr(f):
        output = out.getvalue()
        assert MockNN is si.nn
        assert MockDS is si.ds
        assert MockNN.called
        assert MockDS.called     
        ### use patch side_effect in multiple functions
        with patch.muptile("s1.nn",
                   _get_data = _func_get_data_side_effect,
                   _random = _func_randome_side_effect
                          )
                           

def main():
  suite = unittest.TestSuite()
  suite.addTest(SI_test('test'))
  unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == "__main__":
  unittest.main()

