import operator
import json
import jsonpickle

class Process():
  def __init__(self, pid, bt, art):
    self.pid = pid
    self.bt = int(bt)
    self.art = int(art)
    self.preemtTime = 0
    self.wt = 0
    self.tat = 0

  def __str__(self):
    return 'Process_id:  ' + self.pid + '\tBurst_time:  ' + self.bt + '\tArrival_time  ' + self.art 

      
class Wrapper():

  def __init__(self,totalExecutionTime, avgTAT, avgWaitingTime,ganttChart):
    self.totalExecutionTime = totalExecutionTime
    self.avgTAT = avgTAT
    self.avgWaitingTime = avgWaitingTime
    self.ganttChart = ganttChart

class Schedular():
  # ganttChart = []

  @staticmethod
  def FCFS( process = [], *args):
    # resting the ganttChart
    ganttChart = []

    # sorting the processes on the bases of arival time
    process.sort(key=operator.attrgetter('art'))
      

    while len(process) != 0 :
      if len(ganttChart) == 0 :
        process[0].preemtTime = process[0].art + process[0].bt
      else:
        process[0].preemtTime = process[0].bt + ganttChart[len(ganttChart)-1].preemtTime
        if (process[0].art - ganttChart[len(ganttChart)-1].preemtTime) > 0 :
            process[0].preemtTime = process[0].preemtTime + (process[0].art - ganttChart[len(ganttChart)-1].preemtTime)

      process[0].tat = process[0].preemtTime - process[0].art
      process[0].wt = process[0].preemtTime - (process[0].art + process[0].bt)
      ganttChart.append(process.pop(0))  


    avgWaitingTime = 0
    avgTAT = 0
    totalExecutionTime = 0

    for x in ganttChart :
      avgWaitingTime += x.wt
      avgTAT += x.tat
      totalExecutionTime += x.bt

    avgTAT = avgTAT/len(ganttChart)
    avgWaitingTime = avgWaitingTime/len(ganttChart) 

    data_warpper = Wrapper(totalExecutionTime, avgTAT, avgWaitingTime, ganttChart)
    data_warpper = jsonpickle.encode(data_warpper,unpicklable=False)

    return data_warpper 

  @staticmethod
  def SJF( process = [], *args):
    
    ganttChart = []
    queue = []

    time = min(process,key=operator.attrgetter('art')).art
    while len(process) != 0 :
      i = 0
      while i < len(process) :
        if process[i].art <= time :
          queue.append(process.pop(i))
          i = i - 1
        i = i + 1 

      if len(queue) == 0:
        time = min(process,key=operator.attrgetter('art')).art
      elif len(queue) > 1:
        queue.sort(key=operator.attrgetter('bt')) 

      while len(queue) != 0 :
        if len(ganttChart) == 0 :
          queue[0].preemtTime = queue[0].art + queue[0].bt
        else :
          queue[0].preemtTime = queue[0].bt + ganttChart[len(ganttChart)-1].preemtTime 
          if (queue[0].art - ganttChart[len(ganttChart)-1].preemtTime) > 0 :
            queue[0].preemtTime = queue[0].preemtTime +  (queue[0].art - ganttChart[len(ganttChart)-1].preemtTime)

        time = time + queue[0].bt
        queue[0].tat = queue[0].preemtTime - queue[0].art
        queue[0].wt = queue[0].preemtTime - (queue[0].art + queue[0].bt)
        ganttChart.append(queue.pop(0))
  
    avgWaitingTime = 0
    avgTAT = 0
    totalExecutionTime = 0

    for x in ganttChart :
      avgWaitingTime += x.wt
      avgTAT += x.tat
      totalExecutionTime += x.bt

    avgTAT = avgTAT/len(ganttChart)
    avgWaitingTime = avgWaitingTime/len(ganttChart) 

    data_warpper = Wrapper(totalExecutionTime, avgTAT, avgWaitingTime, ganttChart)
    data_warpper = jsonpickle.encode(data_warpper,unpicklable=False)

    return data_warpper

