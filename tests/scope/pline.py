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

### Testing API Calls
### a unit test to generate random input data and run a single step of gradient descent. assert the step to complete without runtime errors.

### Testing for Algorithmic Correctness
### Train the model for a few iterations and verify that the loss decreases.
### Train the algorithm without regularization. If the model is complex enough, it will memorize the training data and the training loss will be close to 0.
### Test specific subcomputations of the algorithm. For example, test that a part of the RNN runs once per element of the input data.

### Integration tests for Pipeline Components

### Validate Model Quality before Serving

### Validate Model-Infra Compatibility before Serving

def test(MockPlineFE , MockPlineDE):
     si.nn()
     si.ds()
     assert MockPlineFE is si.PlineFE
     assert MockPlineDE is si.PlineDE
     assert MockPlineFE .called
     assert MockPlineDE.called
     
