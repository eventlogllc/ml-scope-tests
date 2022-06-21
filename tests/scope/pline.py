from unittest.mock import patch

@patch('si.pline.feature_extraction')
@patch('si.pline.model_evaluation')
@patch('si.pline.evaluation')
### what
### the GOAL of this test is to
######## Writing appropriate tests for launch and production.
######## Detecting failure modes in your ML pipeline using tests.
######## Evaluating the model quality in production.

### how 
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
     
