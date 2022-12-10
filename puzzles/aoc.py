import copy
import inspect
import os
import time
import sys


class Puzzle:
    
    # The delimiter to use to separate the input data into a list for subsequent
    # processing. E.g. '\n', ',', etc. Set to None to read the data in whole.
    # Delimited items can be processed prior to being added to the input list by
    # overriding _process_input_item().
    # The resulting list, or the raw data if `input_delimiter = None`, can be
    # processed by overriding _process_input_data().
    input_delimiter = '\n'
    
    # By default, strip leading/trailing whitespace from each processed input
    # item (as dictated by `input_delimiter`), or from the whole input itself
    # (when `input_delimiter = None`). Can be disabled for puzzle inputs in
    # which leading/trailing whitespace is important.
    strip_whitespace = True
    
    def __init__(self, sample=False, verbosity=2):
        
        self.sample = sample
        self.verbosity = verbosity
    
    def get_input_file_name(self):
        
        path = os.path.dirname(os.path.abspath(inspect.getfile(self.__class__)))
        filename = 'sample' if self.sample else 'input'
        
        return os.path.join(path, filename)
    
    def parse_string(self, value):
        
        if self.strip_whitespace:
            value = value.strip()
        
        return value
    
    def process_input_item(self, input_line):
        
        return input_line
    
    def process_input_data(self, input_data):
        
        return input_data
    
    def get_input(self):
        
        start = time.time()
        
        input_file = self.get_input_file_name()
        delimiter = self.input_delimiter
        parse = self.parse_string
        process_item = self.process_input_item
        
        input_size = 0
        item_type = 'bytes'
        if delimiter == '\n':
            item_type = 'lines'
        elif delimiter:
            item_type = 'items'
        
        with open(input_file, 'r') as f:
            input_data = parse(f.read())  # optionally trim whitespace (e.g. newlines)
            
            if delimiter:
                # Optionally trim whitespace from and process each item in the
                # raw input data after applying the configured delimiter
                input_data = [process_item(parse(item)) for item in input_data.split(delimiter)]
                input_size = len(input_data)
            else:
                # No delimiter in use, just report the size of the input file
                # in bytes
                input_size = sys.getsizeof(input_data)
            
            # Apply any overall processing of the input data
            input_data = self.process_input_data(input_data)
        
        t = time.time() - start
        
        print(f'Raw input: {input_size} {item_type} (processed into {type(input_data)}) [{t:.6f}s]')
        
        return input_data
    
    def _do_solve(self, solvers):
        
        v = self.verbosity
        max_v = v > 1
        
        # Get input
        if max_v:
            sample = '**SAMPLE** ' if self.sample else ''
            print('=' * 50, f'\n\nReading {sample}input...')
        
        try:
            input_data = self.get_input()
        except FileNotFoundError:
            print(f'No input data file found (looked in {self.get_input_file_name()}).')
            return
        
        # Run solvers
        for part, solver in solvers:
            # Copy the data so each part is free to manipulate it without
            # affecting subsequent parts
            part_input_data = copy.deepcopy(input_data)
            
            if max_v:
                print('\nSolving ', end='')
            
            print(f'Part {part}... ', end='\n' if max_v else '')
            
            start = time.time()
            solution = solver(part_input_data)
            t = time.time() - start
            
            if max_v:
                print('Solution: ', end='')
            
            print(f'{solution} [{t:.6f}s]')
        
        if max_v:
            print('\n', '=' * 50, sep='')
    
    def _part1(self, input_data):
        
        raise NotImplementedError()
    
    def _part2(self, input_data):
        
        raise NotImplementedError()
    
    def solve_part1(self):
        
        self._do_solve([(1, self._part1)])
    
    def solve_part2(self):
        
        self._do_solve([(2, self._part2)])
    
    def solve(self):
        
        self._do_solve([(1, self._part1), (2, self._part2)])
