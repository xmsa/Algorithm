class Binary_Search:
    @staticmethod
    def __recursive_binary_search(lst, value):
        """
        Recursive binary search
        Parameters:
            lst: list
                The list
            value: int,float, ...
                Search value

        Returns:
            int:
            index of element in list
            If it does not find the desired value, it returns -1
        """
        if len(lst) == 0:
            return -1

        median = int(len(lst) // 2)
        if lst[median] == value:
            return median
        elif lst[median] < value:
            flag = Binary_Search.__recursive_binary_search(
                lst[median + 1:], value)
            if flag == -1:
                return -1
            return flag + median + 1
        elif lst[median] > value:
            return Binary_Search.__recursive_binary_search(lst[:median], value)
        else:
            return -1

    @staticmethod
    def __non_recursive_binary_search(lst, value):
        """
        non-Recursive binary search
        Parameters:
            lst: list
                The list
            value: int,float, ...
                Search value

        Returns:
            int:
            index of element in list
            If it does not find the desired value, it returns -1
        """
        i, j = 0, len(lst)
        while i < j:
            median = (i + j) // 2

            if lst[median] == value:
                return median
            elif lst[median] < value:
                i = median + 1
            elif lst[median] > value:
                j = median
            else:
                return -1
        return -1

    @staticmethod
    def binary_search(lst, value, recursive=False):
        """
        Parameters:
            lst: list

            value: int,float, ...
                Search value
            recursive: bool (Defult:False)
                Recursive(True) and non-recursive(False)

        Returns:
            int:
            index of element in list
            If it does not find the desired value, it returns -1
        """

        if not (Binary_Search.is_sort(lst)):
            print("The ascending list is not sort")
            return -1
        if recursive:
            return Binary_Search.__recursive_binary_search(lst, value)
        else:
            return Binary_Search.__non_recursive_binary_search(lst, value)

    @staticmethod
    def is_sort(lst, ascending=True):
        """
        Checks whether the presentation is ascending or descending
        Parameters:
            lst: list
                The list
            ascending: bool, default=True
                Determining ascending or descending

        Returns:
            bool:
            If the list was in order, "true", otherwise "false"
        """
        flag = 0
        for i in range(len(lst) - 1):
            if lst[i] > lst[i + 1] and ascending:

                return False
            elif lst[i] < lst[i + 1] and not (ascending):
                return False

        return True
