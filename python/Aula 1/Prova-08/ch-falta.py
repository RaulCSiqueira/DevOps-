import time

class BlockTimer:
    ''' Times how long it takes for the block of code to complete. 
    

        Requirements:
            Implement the context manager protocol for this class.

            Call the set_start_time method when entering the context.
            Call the set_close_time method when exiting the context.

        Example Usage:
            with BlockTimer():
                something_sorta_slow()
    '''
    
    def set_start_time(self):
        self.start = time.perf_counter()

    def set_close_time(self):
        close = time.perf_counter()
        print(f'block completed in {close - self.start:0.5f} seconds.')

        

def something_sorta_slow():
    return ''.join([str(n) for n in range(1_000_000) if n % 10_000 == 0.0])

if __name__ == '__main__':

    with BlockTimer():
        something_sorta_slow()
        something_sorta_slow()