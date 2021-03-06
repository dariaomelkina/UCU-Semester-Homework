from modules.list import List
from modules.linked_list import LinkedList, LinkedListNode
from modules.multi_linked_list import DoubleMLinkedList, TripleMLinkedList


class WeatherData:
    """ Class for weather data container representation. """

    def __init__(self, data):
        """
        (WeatherData) -> NoneType
        Create new weather data container.
        """
        self._data = data
        self._week_list = List(7)
        for i in range(len(self._week_list)):
            self._week_list[i] = List(4)
        self._graphs_data_list = TripleMLinkedList('week')
        self._graphs_data_list.head().one_way = List(3)
        self._graphs_data_list.head().second_way = List(3)
        self._graphs_data_list.head().third_way = List(3)
        self._days_list = List(7)
        self.extract_data()

    def extract_data(self):
        """
        (WeatherData) -> NoneType
        Extract data from the json and place it in the container.
        """
        # make a dictionary with information
        dict_with_day_data = dict()
        for key in self._data.keys():
            if key in self._data['sol_keys']:
                dict_with_day_data[key] = self._data[key]
                self._days_list.add(key)

        # add information for each day
        for i in range(7):
            t_list = List(3)
            p_list = List(3)
            s_list = List(3)

            sol = self._days_list[i]
            self._week_list[i][0] = sol
            self._week_list[i][1] = TripleMLinkedList('tps')

            t_list[0] = LinkedListNode(dict_with_day_data[sol]['AT']['mn'])
            t_list[1] = LinkedListNode(dict_with_day_data[sol]['AT']['mx'])
            t_list[2] = LinkedListNode(dict_with_day_data[sol]['AT']['av'])

            p_list[0] = LinkedListNode(dict_with_day_data[sol]['PRE']['mn'])
            p_list[1] = LinkedListNode(dict_with_day_data[sol]['PRE']['mx'])
            p_list[2] = LinkedListNode(dict_with_day_data[sol]['PRE']['av'])

            s_list[0] = LinkedListNode(dict_with_day_data[sol]['HWS']['mn'])
            s_list[1] = LinkedListNode(dict_with_day_data[sol]['HWS']['mx'])
            s_list[2] = LinkedListNode(dict_with_day_data[sol]['HWS']['av'])

            self._week_list[i][1].one_way = t_list
            self._week_list[i][1].second_way = p_list
            self._week_list[i][1].third_way = s_list

            self._week_list[i][2] = DoubleMLinkedList('wr')

            temp = [i for i in dict_with_day_data[sol]['WD']][0]
            ct = LinkedList(dict_with_day_data[sol]['WD'][temp]['ct'])
            dg = LinkedList(dict_with_day_data[sol]['WD'][temp]['compass_degrees'])

            for key in dict_with_day_data[sol]['WD']:
                if key != temp:
                    ct.add(dict_with_day_data[sol]['WD'][key]['ct'])
                    dg.add(dict_with_day_data[sol]['WD'][key]['compass_degrees'])

            self._week_list[i][2].one_way = ct
            self._week_list[i][2].second_way = dg

            self._week_list[i][3] = dict_with_day_data[sol]['Season']

        # connect information for all the days tmin
        self._graphs_data_list.head().one_way[0] = LinkedList('tmin')
        node = self._graphs_data_list.head().one_way[0].head()
        for i in range(7):
            node.next = self._week_list[i][1].one_way[0]
            node = node.next

        # connect information for all the days tmax
        self._graphs_data_list.head().one_way[1] = LinkedList('tmax')
        node = self._graphs_data_list.head().one_way[1].head()
        for i in range(7):
            node.next = self._week_list[i][1].one_way[1]
            node = node.next

        # connect information for all the days tav
        self._graphs_data_list.head().one_way[2] = LinkedList('tav')
        node = self._graphs_data_list.head().one_way[2].head()
        for i in range(7):
            node.next = self._week_list[i][1].one_way[2]
            node = node.next

        # connect information for all the days pmin
        self._graphs_data_list.head().second_way[0] = LinkedList('pmin')
        node = self._graphs_data_list.head().second_way[0].head()
        for i in range(7):
            node.next = self._week_list[i][1].second_way[0]
            node = node.next

        # connect information for all the days pmax
        self._graphs_data_list.head().second_way[1] = LinkedList('pmax')
        node = self._graphs_data_list.head().second_way[1].head()
        for i in range(7):
            node.next = self._week_list[i][1].second_way[1]
            node = node.next

        # connect information for all the days pav
        self._graphs_data_list.head().second_way[2] = LinkedList('pav')
        node = self._graphs_data_list.head().second_way[2].head()
        for i in range(7):
            node.next = self._week_list[i][1].second_way[2]
            node = node.next

        # connect information for all the days smin
        self._graphs_data_list.head().third_way[0] = LinkedList('smin')
        node = self._graphs_data_list.head().third_way[0].head()
        for i in range(7):
            node.next = self._week_list[i][1].third_way[0]
            node = node.next

        # connect information for all the days smax
        self._graphs_data_list.head().third_way[1] = LinkedList('smax')
        node = self._graphs_data_list.head().third_way[1].head()
        for i in range(7):
            node.next = self._week_list[i][1].third_way[1]
            node = node.next

        # connect information for all the days sav
        self._graphs_data_list.head().third_way[2] = LinkedList('sav')
        node = self._graphs_data_list.head().third_way[2].head()
        for i in range(7):
            node.next = self._week_list[i][1].third_way[2]
            node = node.next

    def days_list(self):
        """
        (WeatherData) -> List
        Return a list with sols (days) numbers.
        """
        return self._days_list

    def day(self, n):
        """
        (WeatherData, int) -> List
        Return a list with information about the day.
        (sol, average temperature, pressure, wind speed)
        """
        result = List(4)
        result[0] = self._week_list[n][0]
        result[1] = self._week_list[n][1].one_way[2].item
        result[2] = self._week_list[n][1].second_way[2].item
        result[3] = self._week_list[n][1].third_way[2].item
        return result

    def season(self, n):
        """
        (WeatherData, int) -> str
        Return season corresponding to the day.
        """
        return self._week_list[n][3]

    def wind_rose(self, n):
        """
        (WeatherData, int) -> LinkedList
        Return linked list with data for n-th day wind rose.
        """
        ct = List(len(self._week_list[n][2].one_way))
        node = self._week_list[n][2].one_way.head()
        while node is not None:
            ct.add(node.item)
            node = node.next
        dg = List(len(self._week_list[n][2].one_way))
        node = self._week_list[n][2].second_way.head()
        while node is not None:
            dg.add(node.item)
            node = node.next
        wr = LinkedList(ct)
        wr.head().next = dg
        return wr

    def min_temp(self):
        """
        (WeatherData) -> List
        Return list with minimum temperatures of the week.
        """
        result = List(7)
        node = self._graphs_data_list.head().one_way[0].head().next
        while node is not None:
            result.add(node.item)
            node = node.next
        return result

    def max_temp(self):
        """
        (WeatherData) -> List
        Return list with maximum temperatures of the week.
        """
        result = List(7)
        node = self._graphs_data_list.head().one_way[1].head().next
        while node is not None:
            result.add(node.item)
            node = node.next
        return result

    def av_temp(self):
        """
        (WeatherData) -> List
        Return list with average temperatures of the week.
        """
        result = List(7)
        node = self._graphs_data_list.head().one_way[2].head().next
        while node is not None:
            result.add(node.item)
            node = node.next
        return result

    def min_pres(self):
        """
        (WeatherData) -> List
        Return list with minimum pressure of the week.
        """
        result = List(7)
        node = self._graphs_data_list.head().second_way[0].head().next
        while node is not None:
            result.add(node.item)
            node = node.next
        return result

    def max_pres(self):
        """
        (WeatherData) -> List
        Return list with maximum pressure of the week.
        """
        result = List(7)
        node = self._graphs_data_list.head().second_way[1].head().next
        while node is not None:
            result.add(node.item)
            node = node.next
        return result

    def av_pres(self):
        """
        (WeatherData) -> List
        Return list with average pressure of the week.
        """
        result = List(7)
        node = self._graphs_data_list.head().second_way[2].head().next
        while node is not None:
            result.add(node.item)
            node = node.next
        return result

    def min_speed(self):
        """
        (WeatherData) -> List
        Return list with minimum wind speed of the week.
        """
        result = List(7)
        node = self._graphs_data_list.head().third_way[0].head().next
        while node is not None:
            result.add(node.item)
            node = node.next
        return result

    def max_speed(self):
        """
        (WeatherData) -> List
        Return list with maximum wind speed of the week.
        """
        result = List(7)
        node = self._graphs_data_list.head().third_way[1].head().next
        while node is not None:
            result.add(node.item)
            node = node.next
        return result

    def av_speed(self):
        """
        (WeatherData) -> List
        Return list with average wind speed of the week.
        """
        result = List(7)
        node = self._graphs_data_list.head().third_way[2].head().next
        while node is not None:
            result.add(node.item)
            node = node.next
        return result
