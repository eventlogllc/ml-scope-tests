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
    ### [why] low-quality data will significantly affect the model's performance, 
    ###       it's much easier to detect low-quality data at input THAN guessing at its existence after the model predicts badly.
    ### [how] rules that the data must satisfy. these rules are the data-schema.
     
### Validating feature engineering. also called engineered-data
    ### [why] while the raw data might be valid, the model only sees engineered feature data. 
    ###       because engineered data looks very different from raw input data, need to check engineered data separately.
    ### [how] unit tests following
    ### All numeric features are scaled, for example, between 0 and 1.
    ### One-hot encoded vectors only contain a single 1 and N-1 zeroes.
    ### Missing data is replaced by mean or default values.
    ### Data distributions after transformation conform to expectations. 
    ###   For example, if you've normalized using z-scores, the mean of the z-scores is 0.
    ### Outliers are handled, such as by scaling or clipping.

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
     
