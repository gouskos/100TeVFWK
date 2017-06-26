'''Filter events based on the number of objects in the input collection.'''

from heppy.framework.analyzer import Analyzer
import collections

class EventFilter  (Analyzer):
    '''Filters events based on the contents of an input collection.
    
    When an event is rejected by the EventFilter, the analyzers
    placed after the filter in the sequence will not run. 

    Example: 

    To reject events with 1 lepton or more: 

    from heppy.analyzers.EventFilter   import EventFilter  
    lepton_filter = cfg.Analyzer(
      EventFilter  ,
      'lepton_filter',
      input_objects = 'leptons',
      min_number = 1,
      veto = True
    )
    
    * input_objects : the input collection.

    * min_number : minimum number of objects in input_objects to trigger the filtering
    
    * veto :
      - if False: events are selected if there are >= min_number objects in input_objects
      - if True: events are rejected if there are >= min_number objects in input_objects.
    '''

    def process(self, event):
        '''event should contain:
        
        * self.cfg_ana.input_objects:
             the list of input_objects to be counted, 
             with the name specified in self.cfg_ana
        '''
        input_collection = getattr(event, self.cfg_ana.input_objects)
        if self.cfg_ana.veto:
            return not len(input_collection) >= self.cfg_ana.min_number
        else:
            return len(input_collection) >= self.cfg_ana.min_number
         

