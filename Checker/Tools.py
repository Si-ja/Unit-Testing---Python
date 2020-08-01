class Functions:

    @staticmethod
    def binary(a, b) -> list():
        """
        Check whether values in respect to their positions
        match per two arrays.

        Parameters
        ----------
        a : list or an array (numpy)
            First list/array holding variable.
        b : list or an array (numpy)
            Second list/array holding variable.

        Returns
        -------
        list()
            A list of True or False boolean values is returned
            on whether values in both of the arreas match or
            not per two different arrays.
        """
        import numpy as np
        answer = []
        if a == [] and b == []:
            return [True]
        try:
            if (a.size == 0 and b.size == 0):
                return [True]
        except:
            pass

        zipper = zip(a, b)
        for data in tuple(zipper):
            if data[0] == data[1]:
                answer.append(True)
            else:
                answer.append(False)

        if len(answer) != (len(a) + len(b)) / 2:
            max_len = 0
            if len(a) > max_len:
                max_len = len(a)
            if len(b) > max_len:
                max_len = len(b)

            for idx in range(max_len + 1):
                if idx <= len(answer):
                    continue
                else:
                    answer.append(False)

        return answer