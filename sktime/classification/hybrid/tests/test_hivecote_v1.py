# -*- coding: utf-8 -*-
"""HIVE-COTE test code."""
# import numpy as np
# from numpy import testing
#
# from sktime.classification.hybrid import HIVECOTEV1
# from sktime.contrib.vector_classifiers._rotation_forest import RotationForest
# from sktime.datasets import load_unit_test


# def test_hivecote_v1_on_unit_test():
#     """Test of HIVECOTEV1 on unit test data."""
#     # load unit test data
#     X_train, y_train = load_unit_test(split="train", return_X_y=True)
#     X_test, y_test = load_unit_test(split="test", return_X_y=True)
#     indices = np.random.RandomState(0).permutation(10)
#
#     # train HIVE-COTE v1
#     rotf = RotationForest(n_estimators=10)
#     hc1 = HIVECOTEV1(
#         random_state=0,
#         stc_params={"estimator": rotf, "transform_limit_in_mins": 0.05},
#         tsf_params={"n_estimators": 10},
#         rise_params={"n_estimators": 10},
#         cboss_params={"n_parameter_samples": 25, "max_ensemble_size": 5},
#     )
#     hc1.fit(X_train.iloc[indices], y_train[indices])
#
#     # assert probabilities are the same
#     probas = hc1.predict_proba(X_test.iloc[indices])
#     testing.assert_array_equal(probas, hivecote_v1_unit_test_probas)


# hivecote_v1_unit_test_probas = np.array(
#     []
# )


# def print_array(array):
#     print('[')
#     for sub_array in array:
#         print('[')
#         for value in sub_array:
#             print(value.astype(str), end='')
#             print(', ')
#         print('],')
#     print(']')
#
# if __name__ == "__main__":
#     X_train, y_train = load_unit_test(split="train", return_X_y=True)
#     X_test, y_test = load_unit_test(split="test", return_X_y=True)
#     indices = np.random.RandomState(0).permutation(10)
#
#     rotf = RotationForest(n_estimators=10)
#     hc1 = HIVECOTEV1(
#         random_state=0,
#         stc_params={"estimator": rotf, "transform_limit_in_mins": 0.05},
#         tsf_params={"n_estimators": 10},
#         rise_params={"n_estimators": 10},
#         cboss_params={"n_parameter_samples": 25, "max_ensemble_size": 5},
#     )
#
#     hc1.fit(X_train.iloc[indices], y_train[indices])
#     probas = hc1.predict_proba(X_test.iloc[indices])
#     print_array(probas)
