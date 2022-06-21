from unittest.mock import patch

@patch('si.pline.feature_extraction')
@patch('si.pline.model_evaluation')
@patch('si.pline.evaluation')

### Validating input data.
### Validating feature engineering.
### Validating quality of new model versions.
### Validating serving infrastructure.
### Testing integration between pipeline components.

def test(MockPlineFE , MockPlineDE):
     si.nn()
     si.ds()
     assert MockPlineFE is si.PlineFE
     assert MockPlineDE is si.PlineDE
     assert MockPlineFE .called
     assert MockPlineDE.called
     
