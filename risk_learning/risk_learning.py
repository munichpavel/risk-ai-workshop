# -*- coding: utf-8 -*-

"""Main module."""
def get_classifier_family_name(clf):
    res = str(clf)
    res = res.split('(')[0]
    return res
    #return 'LogisticRegression'