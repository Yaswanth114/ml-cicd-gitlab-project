from train import train_model

def test_accuracy():
    accuracy = train_model()
    assert accuracy > 0.85   
