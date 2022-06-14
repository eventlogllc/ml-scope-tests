from unittest.mock import patch

@patch('si.pline.feature_extraction')
@patch('si.pline.model_evaluation')
@patch('si.pline.evaluation')
def test(MockPlineFE , MockPlineDE):
     si.nn()
     si.ds()
     assert MockPlineFE is si.PlineFE
     assert MockPlineDE is si.PlineDE
     assert MockPlineFE .called
     assert MockPlineDE.called
