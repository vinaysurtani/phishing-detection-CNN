# Purpose - Receive the call for testing a page from the Chrome extension and return the result (SAFE/PHISHING)
# for display. This file calls all the different components of the project (The ML model, features_extraction) and
# consolidates the result.

from tensorflow import keras
import features_extraction
import sys
import numpy as np
import tensorflow as tf
import logging
tf.get_logger().setLevel(logging.ERROR)

from features_extraction import LOCALHOST_PATH, DIRECTORY_NAME


def get_prediction_from_url(test_url):
    features_test = features_extraction.main(test_url)
    # Due to updates to scikit-learn, we now need a 2D array as a parameter to the predict function.
    features_test = np.array(features_test).reshape((1, -1))
    features_test = features_test[...,None]
    model = keras.models.load_model(LOCALHOST_PATH + DIRECTORY_NAME + "\\model\\model.h5")

    pred = model.predict(features_test)
    print(pred[0])
    if(pred[0]>0.7):
        return 1
    else:
        return 0
    #return int(pred[0])


def main():
    url = sys.argv[1]

    prediction = get_prediction_from_url(url)

    # Print the probability of prediction (if needed)
    # prob = clf.predict_proba(features_test)
    # print 'Features=', features_test, 'The predicted probability is - ', prob, 'The predicted label is - ', pred
    #    print "The probability of this site being a phishing website is ", features_test[0]*100, "%"

    if prediction == 1:
        # print "The website is safe to browse"
        print(" SAFE")
    elif prediction == 0:
        # print "The website has phishing features. DO NOT VISIT!"
        print(" PHISHING")

        # print 'Error -', features_test

#if __name__ == "__main__":
main()
