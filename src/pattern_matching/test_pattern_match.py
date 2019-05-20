from unittest import TestCase
from pattern_match import find_best_match_pattern


class TestFind_best_match_pattern(TestCase):
    def sample_patterns(self):
        # provided by the problem statement
        patterns = ['*,b,*',
                    'a,*,*',
                    '*,*,c',
                    'foo,bar,baz',
                    'w,x,*,*',
                    '*,x,y,z',
                    ]
        return patterns

    def sample_paths(self):
        # provided by the problem statement
        paths = ['/w/x/y/z/',
                 'a/b/c',
                 'foo/',
                 'foo/bar/',
                 'foo/bar/baz/',
                 ]
        return paths

    def robust_paths(self):
        # include more edge cases than the sample inputs
        paths = ['/w/x/y/z/',
                 'a/b/c',
                 '123/b/c',
                 '/foo/',
                 'foo/bar/',
                 'foo/bar/baz/',
                 '/foo/bar/baz',
                 '/123/']
        return paths

    def robust_patterns(self):
        # include more edge cases than the sample inputs
        patterns = ['*,b,*',
                    '123,*,*',
                    'S,*,*',
                    '*,*,c',
                    'a,*,*',
                    'foo,bar,baz',
                    'w,x,*,z',
                    '*,*,*,*',
                    '*,x,y,z',
                    '*',
                    'Foo',
                    'foo',
                    '123'
                    ]
        return patterns

    def test_find_best_match_pattern_sample_input(self):
        matches = [find_best_match_pattern(path, self.sample_patterns()) for path in self.sample_paths()]
        self.assertEqual(matches, ['*,x,y,z', 'a,*,*', 'NO MATCH', 'NO MATCH', 'foo,bar,baz'])

    def test_find_best_match_pattern_robust_input(self):
        matches = [find_best_match_pattern(path, self.robust_patterns()) for path in self.robust_paths()]
        self.assertEqual(matches,
                         ['w,x,*,z', 'a,*,*', '123,*,*', 'foo', 'NO MATCH', 'foo,bar,baz', 'foo,bar,baz', '123'])
