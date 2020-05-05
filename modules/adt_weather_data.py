from modules.list import List
from modules.linked_list import LinkedList, LinkedListNode
from modules.multi_linked_list import DoubleMLinkedList, TripleMLinkedList


class WeatherData:
    def __init__(self, data):
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

    def days_list(self):
        return self._days_list

    def day(self, n):
        result = List(10)
        result[0] = self._week_list[n][0]
        result[1] = self._week_list[n][1].one_way[0].item
        result[2] = self._week_list[n][1].one_way[1].item
        result[3] = self._week_list[n][1].one_way[2].item
        result[4] = self._week_list[n][1].second_way[0].item
        result[5] = self._week_list[n][1].second_way[1].item
        result[6] = self._week_list[n][1].second_way[2].item
        result[7] = self._week_list[n][1].third_way[0].item
        result[8] = self._week_list[n][1].third_way[1].item
        result[9] = self._week_list[n][1].third_way[2].item
        return result

    def season(self, n):
        return self._week_list[n][3]

    def wind_rose(self, n):
        wr = LinkedList(self._week_list[n][2].one_way)
        wr.head().next = self._week_list[n][2].second_way
        return wr

    def min_temp(self):
        result = List(7)
        node = self._graphs_data_list.head().one_way[0].head().next
        while node is not None:
            result.add(node.item)
            node = node.next
        return result

    def max_temp(self):
        pass

    def av_temp(self):
        pass

    def min_pres(self):
        pass

    def max_pres(self):
        pass

    def av_pres(self):
        pass

    def min_speed(self):
        pass

    def max_speed(self):
        pass

    def av_speed(self):
        pass
