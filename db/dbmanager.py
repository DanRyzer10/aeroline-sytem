import sqlalchemy
import abc

#create abstract clase
class DbManager(abc.ABC):
    @abc.abstractmethod
    def connect(self, host, port, service_name):
        pass

    @abc.abstractmethod
    def disconnect(self):
        pass

    @abc.abstractmethod
    def execute(self, query):
        pass

    @abc.abstractmethod
    def executemany(self, query, data):
        pass

    @abc.abstractmethod
    def commit(self):
        pass

    @abc.abstractmethod
    def rollback(self):
        pass

    @abc.abstractmethod
    def fetchone(self):
        pass

    @abc.abstractmethod
    def fetchmany(self, size):
        pass

    @abc.abstractmethod
    def fetchall(self):
        pass

    @abc.abstractmethod
    def close(self):
        pass




    