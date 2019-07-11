"""Tests for `risk_learning` package."""
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import GradientBoostingClassifier

from risk_learning.risk_learning import get_classifier_family_name

def test_get_classifier_family_name():
    assert get_classifier_family_name(LogisticRegression()) == 'LogisticRegression'
    assert get_classifier_family_name(GradientBoostingClassifier()) == 'GradientBoostingClassifier'
