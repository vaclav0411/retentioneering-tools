from retentioneering import init_config
from retentioneering import datasets

data = datasets.load_simple_shop()


# setup init_config and apply retention.prepare()
init_config(
    experiments_folder='experiments', # folder for saving experiment results: graph visualization, heatmaps and etc.
    index_col='client_id', # column by which we split users / sessions / whatever
    event_col='event', # column that describes event
    event_time_col='timestamp', # column that describes timestamp of event
    positive_target_event='passed', # name of positive target event
    negative_target_event='lost', # name of negative target event
    pos_target_definition={ # how to define positive event, e.g. empty means that add passed for whom was not 'lost'
        'event_list': ['payment_done']
    },
    neg_target_definition={}
)
data = data.retention.prepare()


# Test if sample dataset imported correctly
def test_import():
    assert len(data) == 35357