from Project1.src.LogisticRegression import LogisticRegression
from Project1.src.NaiveBayes import NaiveBayes
from Project1.src.Processor import Processor
from Project1.src.Clean import Clean
from Project1.src.CrossValidation import cross_validation
import timeit
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def df_to_table(pandas_frame, export_filename):
    fig, ax = plt.subplots()

    fig.patch.set_visible(False)
    ax.axis('off')
    ax.axis('tight')

    ax.table(cellText=pandas_frame.values, colLabels=pandas_frame.columns, loc='center')

    fig.tight_layout()

    plt.savefig(export_filename + '.png', bbox_inches='tight')

ds = "adult"

if ds == "adult":
    """ADULT"""


    a_setup_NB = '''
from Project1.src.NaiveBayes import NaiveBayes
from Project1.src.LogisticRegression import LogisticRegression
from Project1.src.Processor import Processor
from Project1.src.Clean import Clean
from Project1.src.CrossValidation import cross_validation

path = "../datasets/adult/adult.data"

header = ['age', 'workclass', 'fnlwgt', 'education', 'education-num', 'marital-status', 'occupation',
          'relationship',
          'race', 'sex', 'capital-gain', 'capital-loss', 'hours-per-week', 'native-country', 'salary']

All = Processor.read(path, header)

[X, Y] = Clean.adult(All)



[X_train, X_test, Y_train, Y_test] = Processor.split(X, Y, train=0.8)

model = NaiveBayes()
    '''

    a_setup_LR = '''
from Project1.src.NaiveBayes import NaiveBayes
from Project1.src.LogisticRegression import LogisticRegression
from Project1.src.Processor import Processor
from Project1.src.Clean import Clean
from Project1.src.CrossValidation import cross_validation

path = "../datasets/adult/adult.data"

header = ['age', 'workclass', 'fnlwgt', 'education', 'education-num', 'marital-status', 'occupation',
          'relationship',
          'race', 'sex', 'capital-gain', 'capital-loss', 'hours-per-week', 'native-country', 'salary']

All = Processor.read(path, header)

[X, Y] = Clean.adult(All)



[X_train, X_test, Y_train, Y_test] = Processor.split(X, Y, train=0.8)

model = LogisticRegression()
        '''

    a_test_NB = '''
w = model.fit(X_train.to_numpy(), Processor.ToNumpyCol(Y_train))
        '''

    a_test_LR = '''
w = model.fit(X_train.to_numpy(), Processor.ToNumpyCol(Y_train), learning_rate=0.2, max_gradient=1e-1, max_iters=20000)
    '''
    print("timing adult")
    #a_timeNB = timeit.timeit(setup=a_setup_NB, stmt=a_test_NB, number=1000) / 1000
    #a_timeLR = timeit.timeit(setup=a_setup_LR, stmt=a_test_LR, number=1000) / 1000
    a_timeNB = timeit.timeit(setup=a_setup_NB, stmt=a_test_NB, number=100) / 100
    a_timeLR = timeit.timeit(setup=a_setup_LR, stmt=a_test_LR, number=100) / 100
    print("done")

    """IONOSPHERE"""

    i_setup_NB = '''
from Project1.src.NaiveBayes import NaiveBayes
from Project1.src.LogisticRegression import LogisticRegression
from Project1.src.Processor import Processor
from Project1.src.Clean import Clean
from Project1.src.CrossValidation import cross_validation

path = "../datasets/ionosphere/ionosphere.data"

header = ["{}{}".format("col", x) for x in range(33 + 1)]
header.append("signal")

All = Processor.read(path, header)

[X, Y] = Clean.Ionosphere(All)

[X_train, X_test, Y_train, Y_test] = Processor.split(X, Y, train=0.8)

model = NaiveBayes()
    '''

    i_setup_LR = '''
from Project1.src.NaiveBayes import NaiveBayes
from Project1.src.LogisticRegression import LogisticRegression
from Project1.src.Processor import Processor
from Project1.src.Clean import Clean
from Project1.src.CrossValidation import cross_validation

path = "../datasets/ionosphere/ionosphere.data"

header = ["{}{}".format("col", x) for x in range(33 + 1)]
header.append("signal")

All = Processor.read(path, header)

[X, Y] = Clean.Ionosphere(All)

[X_train, X_test, Y_train, Y_test] = Processor.split(X, Y, train=0.8)

model = LogisticRegression()
    '''

    i_test_NB = '''
w = model.fit(X_train.to_numpy(), Processor.ToNumpyCol(Y_train))
    '''

    i_test_LR = '''
w = model.fit(X_train.to_numpy(), Processor.ToNumpyCol(Y_train), learning_rate=0.2, max_gradient=1e-2, max_iters=10000)
'''
    print("timing i")
    #i_timeNB = timeit.timeit(setup=i_setup_NB, stmt=i_test_NB, number=1000) / 1000
    #i_timeLR = timeit.timeit(setup=i_setup_LR, stmt=i_test_LR, number=1000) / 1000
    i_timeNB = timeit.timeit(setup=i_setup_NB, stmt=i_test_NB, number=100) / 100
    i_timeLR = timeit.timeit(setup=i_setup_LR, stmt=i_test_LR, number=100) / 100
    print("done")

    """Mamogram"""

    m_setup_NB = '''
from Project1.src.NaiveBayes import NaiveBayes
from Project1.src.LogisticRegression import LogisticRegression
from Project1.src.Processor import Processor
from Project1.src.Clean import Clean
from Project1.src.CrossValidation import cross_validation

path = "../datasets/mam/mam.data"
header = ["BI-RADS", "age", "shape", "margin", "density", "result"]
All = Processor.read(path, header)

[X, Y] = Clean.mam(All)

[X_train, X_test, Y_train, Y_test] = Processor.split(X, Y, train=0.8)

model = NaiveBayes()
        '''

    m_setup_LR = '''
from Project1.src.NaiveBayes import NaiveBayes
from Project1.src.LogisticRegression import LogisticRegression
from Project1.src.Processor import Processor
from Project1.src.Clean import Clean
from Project1.src.CrossValidation import cross_validation

path = "../datasets/mam/mam.data"
header = ["BI-RADS", "age", "shape", "margin", "density", "result"]
All = Processor.read(path, header)

[X, Y] = Clean.mam(All)

[X_train, X_test, Y_train, Y_test] = Processor.split(X, Y, train=0.8)

model = LogisticRegression()
        '''

    m_test_NB = '''
w = model.fit(X_train.to_numpy(), Processor.ToNumpyCol(Y_train))
        '''

    m_test_LR = '''
w = model.fit(X_train.to_numpy(), Processor.ToNumpyCol(Y_train), learning_rate=0.001, max_gradient=1e-1, max_iters=15000)
    '''
    print("timing m")
    #m_timeNB = timeit.timeit(setup=m_setup_NB, stmt=m_test_NB, number=1000) / 1000
    #m_timeLR = timeit.timeit(setup=m_setup_LR, stmt=m_test_LR, number=1000) / 1000
    m_timeNB = timeit.timeit(setup=m_setup_NB, stmt=m_test_NB, number=100) / 100
    m_timeLR = timeit.timeit(setup=m_setup_LR, stmt=m_test_LR, number=100) / 100
    print("done")

    """TICTACTOE"""

    t_setup_NB = '''
from Project1.src.NaiveBayes import NaiveBayes
from Project1.src.LogisticRegression import LogisticRegression
from Project1.src.Processor import Processor
from Project1.src.Clean import Clean
from Project1.src.CrossValidation import cross_validation

path = "../datasets/tictactoe/tic-tac-toe.data"
header = ["tl", "tm", "tr", "ml", "mm", "mr", "bl", "bm", "br", "result"]

All = Processor.read(path, header)

[X, Y] = Clean.ttt(All)

print(X.shape)

[X_train, X_test, Y_train, Y_test] = Processor.split(X, Y, train=0.8)

model = NaiveBayes()
if type(model) == NaiveBayes:
    X_train = X_train.astype('float64')
    Y_train = Y_train.astype('float64')
        '''

    t_setup_LR = '''
from Project1.src.NaiveBayes import NaiveBayes
from Project1.src.LogisticRegression import LogisticRegression
from Project1.src.Processor import Processor
from Project1.src.Clean import Clean
from Project1.src.CrossValidation import cross_validation

path = "../datasets/tictactoe/tic-tac-toe.data"
header = ["tl", "tm", "tr", "ml", "mm", "mr", "bl", "bm", "br", "result"]

All = Processor.read(path, header)

[X, Y] = Clean.ttt(All)

print(X.shape)

[X_train, X_test, Y_train, Y_test] = Processor.split(X, Y, train=0.8)

model = LogisticRegression()
if type(model) == NaiveBayes:
    X_train = X_train.astype('float64')
    Y_train = Y_train.astype('float64')
        '''

    t_test_NB = '''
w = model.fit(X_train.to_numpy(), Processor.ToNumpyCol(Y_train))
            '''

    t_test_LR = '''
w = model.fit(X_train.to_numpy(), Processor.ToNumpyCol(Y_train), learning_rate=0.6, max_gradient=1e-2, max_iters=15000)
        '''

    print("timing t")
    #t_timeNB = timeit.timeit(setup=t_setup_NB, stmt=t_test_NB, number=1000) / 1000
    #t_timeLR = timeit.timeit(setup=t_setup_LR, stmt=t_test_LR, number=1000) / 1000
    t_timeNB = timeit.timeit(setup=t_setup_NB, stmt=t_test_NB, number=100) / 100
    t_timeLR = timeit.timeit(setup=t_setup_LR, stmt=t_test_LR, number=100) / 100
    print("done")

    #print(result)
    data = {'Dataset': ['Adult', 'Ionosphere', 'Mammograph', 'Tic-Tac-Toe'],
            'Execution Time (Naive Bayes)': [a_timeNB, i_timeNB, m_timeNB, t_timeNB],
            'Execution Time (Logistic Regression)' : [a_timeLR, i_timeLR, m_timeLR, t_timeLR]}

    df = pd.DataFrame(data)

    df_to_table(df, 'time_table_all_final')

    # print(evaluate_acc(Processor.ToNumpyCol(Y_test), model.predict(X_test.to_numpy())))

    #print(cross_validation(5, X_train.to_numpy(), Processor.ToNumpyCol(Y_train), model))

elif ds == "ionosphere":
    path = "../datasets/ionosphere/ionosphere.data"

    header = ["{}{}".format("col", x) for x in range(33 + 1)]
    header.append("signal")

    All = Processor.read(path, header)

    [X, Y] = Clean.Ionosphere(All)

    [X_train, X_test, Y_train, Y_test] = Processor.split(X, Y, train=0.8)
    setup = '''
from Project1.src.NaiveBayes import NaiveBayes
from Project1.src.Processor import Processor
from Project1.src.Clean import Clean
from Project1.src.CrossValidation import cross_validation

path = "../datasets/ionosphere/ionosphere.data"

header = ["{}{}".format("col", x) for x in range(33 + 1)]
header.append("signal")

All = Processor.read(path, header)

[X, Y] = Clean.Ionosphere(All)

[X_train, X_test, Y_train, Y_test] = Processor.split(X, Y, train=0.8)

model = NaiveBayes()
'''

    test = '''
w = model.fit(X_train.to_numpy(), Processor.ToNumpyCol(Y_train))
'''

    time = timeit.timeit(setup=setup, stmt=test, number=10000) / 10000
    print(time)

    #print(cross_validation(5, X_train.to_numpy(), Processor.ToNumpyCol(Y_train), model))

elif ds == "mam":
    path = "./datasets/mam/mam.data"
    header = ["BI-RADS", "age", "shape", "margin", "density", "result"]
    All = Processor.read(path, header)

    [X, Y] = Clean.mam(All)

    [X_train, X_test, Y_train, Y_test] = Processor.split(X, Y, train=0.8)

    model = NaiveBayes()

    print(cross_validation(5, X_train.to_numpy(), Processor.ToNumpyCol(Y_train), model))

elif ds == "ttt":
    path = "./datasets/tictactoe/tic-tac-toe.data"
    header = ["tl", "tm", "tr", "ml", "mm", "mr", "bl", "bm", "br", "result"]

    All = Processor.read(path, header)

    [X, Y] = Clean.ttt(All)

    print(X.shape)

    [X_train, X_test, Y_train, Y_test] = Processor.split(X, Y, train=0.8)

    model = NaiveBayes()
    if type(model) == NaiveBayes:
        X_train = X_train.astype('float64')
        Y_train = Y_train.astype('float64')

    print(cross_validation(5, X_train.to_numpy(), Processor.ToNumpyCol(Y_train), model))