from sql_tool import Database as SQL
from sql_vars import queries


class Metric:
    def __init__(self):
        self.id = None
        self.name = None
        self.desc = None

    @staticmethod
    def make_new(metric_name, user_id):
        query = queries['metrics']['new'].format(metric_name=metric_name, user_id=user_id)
        SQL(query).run()

    # def disable(self):

    # def enable(self):

    # def get_info(self):


Metric().make_new(metric_name='test_metric', user_id=1111)
