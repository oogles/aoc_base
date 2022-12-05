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
        
        input_file = self.get_input_file_name()
        delimiter = self.input_delimiter
        parse = self.parse_string
        process_item = self.process_input_item
        
        with open(input_file, 'r') as f:
            if delimiter == '\n':
                # Optionally trim whitespace from and process each line in the input
                # file, skipping any blank lines
                input_data = []
                
                for line in f.readlines():
                    line = parse(line)
                    if line:
                        input_data.append(process_item(line))
            else:
                input_data = parse(f.read())  # optionally trim whitespace (e.g. newlines)
                
                if delimiter:
                    # Optionally trim whitespace from and process each item in the
                    # raw input data after applying the configured delimiter
                    input_data = [process_item(parse(item)) for item in input_data.split(delimiter)]
                
                # Apply any overall processing of the input data
                input_data = self.process_input_data(input_data)
        
        return input_data
    
    def _do_solve(self, solvers):
        
        v = self.verbosity
        max_v = v > 1
        line_endings = '\n' if max_v else ''
        
        # Get input
        if max_v:
            sample = '**SAMPLE** ' if self.sample else ''
            print('=' * 50, f'\n\nProcessing {sample}', end='')
        
        print('Input...  ', end=line_endings)
        
        start = time.time()
        try:
            input_data = self.get_input()
        except FileNotFoundError:
            print(f'No input data file found (looked in {self.get_input_file_name()}).')
            return
        
        t = time.time() - start
        
        if self.input_delimiter == '\n':
            input_desc = f'has {len(input_data)} lines'
        elif self.input_delimiter:
            input_desc = f'has {len(input_data)} items'
        else:
            size = sys.getsizeof(input_data)
            input_desc = f'is {size} bytes'
        
        if max_v:
            print('Input ', end='')
        
        print(f'{input_desc} ({type(input_data)}) [{t:.6f}s]')
        
        # Run solvers
        for part, solver in solvers:
            if self.input_delimiter:
                # Copy the data so each part is free to manipulate it without
                # affecting subsequent parts
                part_input_data = input_data[:]
            else:
                part_input_data = input_data
            
            if max_v:
                print('\nSolving ', end='')
            
            print(f'Part {part}... ', end=line_endings)
            
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
