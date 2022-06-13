from unittest.mock import patch

@patch('si.nn')
@patch('si.ds')
def test(MockNN, MockDS):
     si.nn()
     si.ds()
     assert MockNN is si.nn
     assert MockDS is si.ds
     assert MockNN.called
     assert MockDS.called
