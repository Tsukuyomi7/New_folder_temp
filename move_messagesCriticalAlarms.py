from java.io import FileInputStream
import java.lang
import os
import string
 
propInputStream = FileInputStream("/u02/jms_messagesmove/domain.propertiesCriticalAlarms")
configProps = Properties()
configProps.load(propInputStream)
 
serverUrl = configProps.get("server.url")
Username = configProps.get("username")
Password = configProps.get("password")
 
systemModuleName = configProps.get("system.module.name")
 
CriticalAlarmsaoldServerName = configProps.get("CriticalAlarms.a.old.server.name")
CriticalAlarmsaoldJmsServerName = configProps.get("CriticalAlarms.a.old.jms.server.name")
CriticalAlarmsaoldQueueName = configProps.get("CriticalAlarms.a.old.queue.name")
 
CriticalAlarmsanewTargetedServerName = configProps.get("CriticalAlarms.a.new.targeted.server.name")
CriticalAlarmsanewJmsServerName = configProps.get("CriticalAlarms.a.new.jms.server.name")
CriticalAlarmsanewQueueName = configProps.get("CriticalAlarms.a.new.queue.name")

CriticalAlarmsboldServerName = configProps.get("CriticalAlarms.b.old.server.name")
CriticalAlarmsboldJmsServerName = configProps.get("CriticalAlarms.b.old.jms.server.name")
CriticalAlarmsboldQueueName = configProps.get("CriticalAlarms.b.old.queue.name")
 
CriticalAlarmsbnewTargetedServerName = configProps.get("CriticalAlarms.b.new.targeted.server.name")
CriticalAlarmsbnewJmsServerName = configProps.get("CriticalAlarms.b.new.jms.server.name")
CriticalAlarmsbnewQueueName = configProps.get("CriticalAlarms.b.new.queue.name")

CriticalAlarmscoldServerName = configProps.get("CriticalAlarms.c.old.server.name")
CriticalAlarmscoldJmsServerName = configProps.get("CriticalAlarms.c.old.jms.server.name")
CriticalAlarmscoldQueueName = configProps.get("CriticalAlarms.c.old.queue.name")
 
CriticalAlarmscnewTargetedServerName = configProps.get("CriticalAlarms.c.new.targeted.server.name")
CriticalAlarmscnewJmsServerName = configProps.get("CriticalAlarms.c.new.jms.server.name")
CriticalAlarmscnewQueueName = configProps.get("CriticalAlarms.c.new.queue.name")

CriticalAlarmsdoldServerName = configProps.get("CriticalAlarms.d.old.server.name")
CriticalAlarmsdoldJmsServerName = configProps.get("CriticalAlarms.d.old.jms.server.name")
CriticalAlarmsdoldQueueName = configProps.get("CriticalAlarms.d.old.queue.name")
 
CriticalAlarmsdnewTargetedServerName = configProps.get("CriticalAlarms.d.new.targeted.server.name")
CriticalAlarmsdnewJmsServerName = configProps.get("CriticalAlarms.d.new.jms.server.name")
CriticalAlarmsdnewQueueName = configProps.get("CriticalAlarms.d.new.queue.name")

CriticalAlarmseoldServerName = configProps.get("CriticalAlarms.e.old.server.name")
CriticalAlarmseoldJmsServerName = configProps.get("CriticalAlarms.e.old.jms.server.name")
CriticalAlarmseoldQueueName = configProps.get("CriticalAlarms.e.old.queue.name")
 
CriticalAlarmsenewTargetedServerName = configProps.get("CriticalAlarms.e.new.targeted.server.name")
CriticalAlarmsenewJmsServerName = configProps.get("CriticalAlarms.e.new.jms.server.name")
CriticalAlarmsenewQueueName = configProps.get("CriticalAlarms.e.new.queue.name")

CriticalAlarmsfoldServerName = configProps.get("CriticalAlarms.f.old.server.name")
CriticalAlarmsfoldJmsServerName = configProps.get("CriticalAlarms.f.old.jms.server.name")
CriticalAlarmsfoldQueueName = configProps.get("CriticalAlarms.f.old.queue.name")
 
CriticalAlarmsfnewTargetedServerName = configProps.get("CriticalAlarms.f.new.targeted.server.name")
CriticalAlarmsfnewJmsServerName = configProps.get("CriticalAlarms.f.new.jms.server.name")
CriticalAlarmsfnewQueueName = configProps.get("CriticalAlarms.f.new.queue.name")


CriticalAlarmsgoldServerName = configProps.get("CriticalAlarms.g.old.server.name")
CriticalAlarmsgoldJmsServerName = configProps.get("CriticalAlarms.g.old.jms.server.name")
CriticalAlarmsgoldQueueName = configProps.get("CriticalAlarms.g.old.queue.name")
CriticalAlarmsgnewTargetedServerName = configProps.get("CriticalAlarms.g.new.targeted.server.name")
CriticalAlarmsgnewJmsServerName = configProps.get("CriticalAlarms.g.new.jms.server.name")
CriticalAlarmsgnewQueueName = configProps.get("CriticalAlarms.g.new.queue.name")
CriticalAlarmsholdServerName = configProps.get("CriticalAlarms.h.old.server.name")
CriticalAlarmsholdJmsServerName = configProps.get("CriticalAlarms.h.old.jms.server.name")
CriticalAlarmsholdQueueName = configProps.get("CriticalAlarms.h.old.queue.name")
CriticalAlarmshnewTargetedServerName = configProps.get("CriticalAlarms.h.new.targeted.server.name")
CriticalAlarmshnewJmsServerName = configProps.get("CriticalAlarms.h.new.jms.server.name")
CriticalAlarmshnewQueueName = configProps.get("CriticalAlarms.h.new.queue.name")
CriticalAlarmsioldServerName = configProps.get("CriticalAlarms.i.old.server.name")
CriticalAlarmsioldJmsServerName = configProps.get("CriticalAlarms.i.old.jms.server.name")
CriticalAlarmsioldQueueName = configProps.get("CriticalAlarms.i.old.queue.name")
CriticalAlarmsinewTargetedServerName = configProps.get("CriticalAlarms.i.new.targeted.server.name")
CriticalAlarmsinewJmsServerName = configProps.get("CriticalAlarms.i.new.jms.server.name")
CriticalAlarmsinewQueueName = configProps.get("CriticalAlarms.i.new.queue.name")
CriticalAlarmsjoldServerName = configProps.get("CriticalAlarms.j.old.server.name")
CriticalAlarmsjoldJmsServerName = configProps.get("CriticalAlarms.j.old.jms.server.name")
CriticalAlarmsjoldQueueName = configProps.get("CriticalAlarms.j.old.queue.name")
CriticalAlarmsjnewTargetedServerName = configProps.get("CriticalAlarms.j.new.targeted.server.name")
CriticalAlarmsjnewJmsServerName = configProps.get("CriticalAlarms.j.new.jms.server.name")
CriticalAlarmsjnewQueueName = configProps.get("CriticalAlarms.j.new.queue.name")
CriticalAlarmskoldServerName = configProps.get("CriticalAlarms.k.old.server.name")
CriticalAlarmskoldJmsServerName = configProps.get("CriticalAlarms.k.old.jms.server.name")
CriticalAlarmskoldQueueName = configProps.get("CriticalAlarms.k.old.queue.name")
CriticalAlarmsknewTargetedServerName = configProps.get("CriticalAlarms.k.new.targeted.server.name")
CriticalAlarmsknewJmsServerName = configProps.get("CriticalAlarms.k.new.jms.server.name")
CriticalAlarmsknewQueueName = configProps.get("CriticalAlarms.k.new.queue.name")
CriticalAlarmsloldServerName = configProps.get("CriticalAlarms.l.old.server.name")
CriticalAlarmsloldJmsServerName = configProps.get("CriticalAlarms.l.old.jms.server.name")
CriticalAlarmsloldQueueName = configProps.get("CriticalAlarms.l.old.queue.name")
CriticalAlarmslnewTargetedServerName = configProps.get("CriticalAlarms.l.new.targeted.server.name")
CriticalAlarmslnewJmsServerName = configProps.get("CriticalAlarms.l.new.jms.server.name")
CriticalAlarmslnewQueueName = configProps.get("CriticalAlarms.l.new.queue.name")
CriticalAlarmsmoldServerName = configProps.get("CriticalAlarms.m.old.server.name")
CriticalAlarmsmoldJmsServerName = configProps.get("CriticalAlarms.m.old.jms.server.name")
CriticalAlarmsmoldQueueName = configProps.get("CriticalAlarms.m.old.queue.name")
CriticalAlarmsmnewTargetedServerName = configProps.get("CriticalAlarms.m.new.targeted.server.name")
CriticalAlarmsmnewJmsServerName = configProps.get("CriticalAlarms.m.new.jms.server.name")
CriticalAlarmsmnewQueueName = configProps.get("CriticalAlarms.m.new.queue.name")
CriticalAlarmsnoldServerName = configProps.get("CriticalAlarms.n.old.server.name")
CriticalAlarmsnoldJmsServerName = configProps.get("CriticalAlarms.n.old.jms.server.name")
CriticalAlarmsnoldQueueName = configProps.get("CriticalAlarms.n.old.queue.name")
CriticalAlarmsnnewTargetedServerName = configProps.get("CriticalAlarms.n.new.targeted.server.name")
CriticalAlarmsnnewJmsServerName = configProps.get("CriticalAlarms.n.new.jms.server.name")
CriticalAlarmsnnewQueueName = configProps.get("CriticalAlarms.n.new.queue.name")
CriticalAlarmsooldServerName = configProps.get("CriticalAlarms.o.old.server.name")
CriticalAlarmsooldJmsServerName = configProps.get("CriticalAlarms.o.old.jms.server.name")
CriticalAlarmsooldQueueName = configProps.get("CriticalAlarms.o.old.queue.name")
CriticalAlarmsonewTargetedServerName = configProps.get("CriticalAlarms.o.new.targeted.server.name")
CriticalAlarmsonewJmsServerName = configProps.get("CriticalAlarms.o.new.jms.server.name")
CriticalAlarmsonewQueueName = configProps.get("CriticalAlarms.o.new.queue.name")


 
 
 
connect(userConfigFile=Username,userKeyFile=Password,url=serverUrl)
 
domainRuntime()

while True:
 try:
 
  print 'Getting the target...'
  cd('ServerServices/'+CriticalAlarmsanewTargetedServerName+'/RuntimeService/ServerRuntime/'+CriticalAlarmsanewTargetedServerName+'/JMSRuntime/'+CriticalAlarmsanewTargetedServerName+'.jms/JMSServers/'+CriticalAlarmsanewJmsServerName+'/Destinations/'+systemModuleName +'!'+CriticalAlarmsanewJmsServerName+'@'+CriticalAlarmsanewQueueName+'')
  target = cmo.getDestinationInfo()
  print 'Got the target...'
   
  cd('ServerServices/'+CriticalAlarmsaoldServerName+'/RuntimeService/ServerRuntime/'+CriticalAlarmsaoldServerName+'/JMSRuntime/'+CriticalAlarmsaoldServerName+'.jms/JMSServers/'+CriticalAlarmsaoldJmsServerName+'/Destinations/'+systemModuleName +'!'+CriticalAlarmsaoldJmsServerName+'@'+CriticalAlarmsaoldQueueName+'')
   
  print 'Moving the messages to the new target...'
  cmo.moveMessages('',target)
  print 'Messages have been moved to the target Successfully !!!'
   
  print '======================================='
  print 'Messages from queue: "'+CriticalAlarmsaoldQueueName+'" of "'+CriticalAlarmsaoldServerName+'"have been moved to the new queue: "'+CriticalAlarmsanewQueueName+'" of "'+CriticalAlarmsanewTargetedServerName+'"Successfully !!!'
  print '======================================='
  
  
  print 'Getting the target...'
  cd('ServerServices/'+CriticalAlarmsbnewTargetedServerName+'/RuntimeService/ServerRuntime/'+CriticalAlarmsbnewTargetedServerName+'/JMSRuntime/'+CriticalAlarmsbnewTargetedServerName+'.jms/JMSServers/'+CriticalAlarmsbnewJmsServerName+'/Destinations/'+systemModuleName +'!'+CriticalAlarmsbnewJmsServerName+'@'+CriticalAlarmsbnewQueueName+'')
  target = cmo.getDestinationInfo()
  print 'Got the target...'
   
  cd('ServerServices/'+CriticalAlarmsboldServerName+'/RuntimeService/ServerRuntime/'+CriticalAlarmsboldServerName+'/JMSRuntime/'+CriticalAlarmsboldServerName+'.jms/JMSServers/'+CriticalAlarmsboldJmsServerName+'/Destinations/'+systemModuleName +'!'+CriticalAlarmsboldJmsServerName+'@'+CriticalAlarmsboldQueueName+'')
   
  print 'Moving the messages to the new target...'
  cmo.moveMessages('',target)
  print 'Messages have been moved to the target Successfully !!!'
   
  print '======================================='
  print 'Messages from queue: "'+CriticalAlarmsboldQueueName+'" of "'+CriticalAlarmsboldServerName+'"have been moved to the new queue: "'+CriticalAlarmsbnewQueueName+'" of "'+CriticalAlarmsbnewTargetedServerName+'"Successfully !!!'
  print '======================================='
  
  
  print 'Getting the target...'
  cd('ServerServices/'+CriticalAlarmscnewTargetedServerName+'/RuntimeService/ServerRuntime/'+CriticalAlarmscnewTargetedServerName+'/JMSRuntime/'+CriticalAlarmscnewTargetedServerName+'.jms/JMSServers/'+CriticalAlarmscnewJmsServerName+'/Destinations/'+systemModuleName +'!'+CriticalAlarmscnewJmsServerName+'@'+CriticalAlarmscnewQueueName+'')
  target = cmo.getDestinationInfo()
  print 'Got the target...'
   
  cd('ServerServices/'+CriticalAlarmscoldServerName+'/RuntimeService/ServerRuntime/'+CriticalAlarmscoldServerName+'/JMSRuntime/'+CriticalAlarmscoldServerName+'.jms/JMSServers/'+CriticalAlarmscoldJmsServerName+'/Destinations/'+systemModuleName +'!'+CriticalAlarmscoldJmsServerName+'@'+CriticalAlarmscoldQueueName+'')
   
  print 'Moving the messages to the new target...'
  cmo.moveMessages('',target)
  print 'Messages have been moved to the target Successfully !!!'
   
  print '======================================='
  print 'Messages from queue: "'+CriticalAlarmscoldQueueName+'" of "'+CriticalAlarmscoldServerName+'"have been moved to the new queue: "'+CriticalAlarmscnewQueueName+'" of "'+CriticalAlarmscnewTargetedServerName+'"Successfully !!!'
  print '======================================='
  
  
  print 'Getting the target...'
  cd('ServerServices/'+CriticalAlarmsdnewTargetedServerName+'/RuntimeService/ServerRuntime/'+CriticalAlarmsdnewTargetedServerName+'/JMSRuntime/'+CriticalAlarmsdnewTargetedServerName+'.jms/JMSServers/'+CriticalAlarmsdnewJmsServerName+'/Destinations/'+systemModuleName +'!'+CriticalAlarmsdnewJmsServerName+'@'+CriticalAlarmsdnewQueueName+'')
  target = cmo.getDestinationInfo()
  print 'Got the target...'
   
  cd('ServerServices/'+CriticalAlarmsdoldServerName+'/RuntimeService/ServerRuntime/'+CriticalAlarmsdoldServerName+'/JMSRuntime/'+CriticalAlarmsdoldServerName+'.jms/JMSServers/'+CriticalAlarmsdoldJmsServerName+'/Destinations/'+systemModuleName +'!'+CriticalAlarmsdoldJmsServerName+'@'+CriticalAlarmsdoldQueueName+'')
   
  print 'Moving the messages to the new target...'
  cmo.moveMessages('',target)
  print 'Messages have been moved to the target Successfully !!!'
   
  print '======================================='
  print 'Messages from queue: "'+CriticalAlarmsdoldQueueName+'" of "'+CriticalAlarmsdoldServerName+'"have been moved to the new queue: "'+CriticalAlarmsdnewQueueName+'" of "'+CriticalAlarmsdnewTargetedServerName+'"Successfully !!!'
  print '======================================='
  
  
  print 'Getting the target...'
  cd('ServerServices/'+CriticalAlarmsenewTargetedServerName+'/RuntimeService/ServerRuntime/'+CriticalAlarmsenewTargetedServerName+'/JMSRuntime/'+CriticalAlarmsenewTargetedServerName+'.jms/JMSServers/'+CriticalAlarmsenewJmsServerName+'/Destinations/'+systemModuleName +'!'+CriticalAlarmsenewJmsServerName+'@'+CriticalAlarmsenewQueueName+'')
  target = cmo.getDestinationInfo()
  print 'Got the target...'
   
  cd('ServerServices/'+CriticalAlarmseoldServerName+'/RuntimeService/ServerRuntime/'+CriticalAlarmseoldServerName+'/JMSRuntime/'+CriticalAlarmseoldServerName+'.jms/JMSServers/'+CriticalAlarmseoldJmsServerName+'/Destinations/'+systemModuleName +'!'+CriticalAlarmseoldJmsServerName+'@'+CriticalAlarmseoldQueueName+'')
   
  print 'Moving the messages to the new target...'
  cmo.moveMessages('',target)
  print 'Messages have been moved to the target Successfully !!!'
   
  print '======================================='
  print 'Messages from queue: "'+CriticalAlarmseoldQueueName+'" of "'+CriticalAlarmseoldServerName+'"have been moved to the new queue: "'+CriticalAlarmsenewQueueName+'" of "'+CriticalAlarmsenewTargetedServerName+'"Successfully !!!'
  print '======================================='
  
  
  print 'Getting the target...'
  cd('ServerServices/'+CriticalAlarmsfnewTargetedServerName+'/RuntimeService/ServerRuntime/'+CriticalAlarmsfnewTargetedServerName+'/JMSRuntime/'+CriticalAlarmsfnewTargetedServerName+'.jms/JMSServers/'+CriticalAlarmsfnewJmsServerName+'/Destinations/'+systemModuleName +'!'+CriticalAlarmsfnewJmsServerName+'@'+CriticalAlarmsfnewQueueName+'')
  target = cmo.getDestinationInfo()
  print 'Got the target...'
   
  cd('ServerServices/'+CriticalAlarmsfoldServerName+'/RuntimeService/ServerRuntime/'+CriticalAlarmsfoldServerName+'/JMSRuntime/'+CriticalAlarmsfoldServerName+'.jms/JMSServers/'+CriticalAlarmsfoldJmsServerName+'/Destinations/'+systemModuleName +'!'+CriticalAlarmsfoldJmsServerName+'@'+CriticalAlarmsfoldQueueName+'')
   
  print 'Moving the messages to the new target...'
  cmo.moveMessages('',target)
  print 'Messages have been moved to the target Successfully !!!'
   
  print '======================================='
  print 'Messages from queue: "'+CriticalAlarmsfoldQueueName+'" of "'+CriticalAlarmsfoldServerName+'"have been moved to the new queue: "'+CriticalAlarmsfnewQueueName+'" of "'+CriticalAlarmsfnewTargetedServerName+'"Successfully !!!'
  print '======================================='
  
  print 'Getting the target...'
  cd('ServerServices/'+CriticalAlarmsgnewTargetedServerName+'/RuntimeService/ServerRuntime/'+CriticalAlarmsgnewTargetedServerName+'/JMSRuntime/'+CriticalAlarmsgnewTargetedServerName+'.jms/JMSServers/'+CriticalAlarmsgnewJmsServerName+'/Destinations/'+systemModuleName +'!'+CriticalAlarmsgnewJmsServerName+'@'+CriticalAlarmsgnewQueueName+'')
  target = cmo.getDestinationInfo()
  print 'Got the target...'
   
  cd('ServerServices/'+CriticalAlarmsgoldServerName+'/RuntimeService/ServerRuntime/'+CriticalAlarmsgoldServerName+'/JMSRuntime/'+CriticalAlarmsgoldServerName+'.jms/JMSServers/'+CriticalAlarmsgoldJmsServerName+'/Destinations/'+systemModuleName +'!'+CriticalAlarmsgoldJmsServerName+'@'+CriticalAlarmsgoldQueueName+'')
   
  print 'Moving the messages to the new target...'
  cmo.moveMessages('',target)
  print 'Messages have been moved to the target Successfully !!!'
   
  print '======================================='
  print 'Messages from queue: "'+CriticalAlarmsgoldQueueName+'" of "'+CriticalAlarmsgoldServerName+'"have been moved to the new queue: "'+CriticalAlarmsgnewQueueName+'" of "'+CriticalAlarmsgnewTargetedServerName+'"Successfully !!!'
  print '======================================='
  
  print 'Getting the target...'
  cd('ServerServices/'+CriticalAlarmshnewTargetedServerName+'/RuntimeService/ServerRuntime/'+CriticalAlarmshnewTargetedServerName+'/JMSRuntime/'+CriticalAlarmshnewTargetedServerName+'.jms/JMSServers/'+CriticalAlarmshnewJmsServerName+'/Destinations/'+systemModuleName +'!'+CriticalAlarmshnewJmsServerName+'@'+CriticalAlarmshnewQueueName+'')
  target = cmo.getDestinationInfo()
  print 'Got the target...'
   
  cd('ServerServices/'+CriticalAlarmsholdServerName+'/RuntimeService/ServerRuntime/'+CriticalAlarmsholdServerName+'/JMSRuntime/'+CriticalAlarmsholdServerName+'.jms/JMSServers/'+CriticalAlarmsholdJmsServerName+'/Destinations/'+systemModuleName +'!'+CriticalAlarmsholdJmsServerName+'@'+CriticalAlarmsholdQueueName+'')
   
  print 'Moving the messages to the new target...'
  cmo.moveMessages('',target)
  print 'Messages have been moved to the target Successfully !!!'
   
  print '======================================='
  print 'Messages from queue: "'+CriticalAlarmsholdQueueName+'" of "'+CriticalAlarmsholdServerName+'"have been moved to the new queue: "'+CriticalAlarmshnewQueueName+'" of "'+CriticalAlarmshnewTargetedServerName+'"Successfully !!!'
  print '======================================='
  
  
  print 'Getting the target...'
  cd('ServerServices/'+CriticalAlarmsinewTargetedServerName+'/RuntimeService/ServerRuntime/'+CriticalAlarmsinewTargetedServerName+'/JMSRuntime/'+CriticalAlarmsinewTargetedServerName+'.jms/JMSServers/'+CriticalAlarmsinewJmsServerName+'/Destinations/'+systemModuleName +'!'+CriticalAlarmsinewJmsServerName+'@'+CriticalAlarmsinewQueueName+'')
  target = cmo.getDestinationInfo()
  print 'Got the target...'
   
  cd('ServerServices/'+CriticalAlarmsioldServerName+'/RuntimeService/ServerRuntime/'+CriticalAlarmsioldServerName+'/JMSRuntime/'+CriticalAlarmsioldServerName+'.jms/JMSServers/'+CriticalAlarmsioldJmsServerName+'/Destinations/'+systemModuleName +'!'+CriticalAlarmsioldJmsServerName+'@'+CriticalAlarmsioldQueueName+'')
   
  print 'Moving the messages to the new target...'
  cmo.moveMessages('',target)
  print 'Messages have been moved to the target Successfully !!!'
   
  print '======================================='
  print 'Messages from queue: "'+CriticalAlarmsioldQueueName+'" of "'+CriticalAlarmsioldServerName+'"have been moved to the new queue: "'+CriticalAlarmsinewQueueName+'" of "'+CriticalAlarmsinewTargetedServerName+'"Successfully !!!'
  print '======================================='
  
  
  print 'Getting the target...'
  cd('ServerServices/'+CriticalAlarmsjnewTargetedServerName+'/RuntimeService/ServerRuntime/'+CriticalAlarmsjnewTargetedServerName+'/JMSRuntime/'+CriticalAlarmsjnewTargetedServerName+'.jms/JMSServers/'+CriticalAlarmsjnewJmsServerName+'/Destinations/'+systemModuleName +'!'+CriticalAlarmsjnewJmsServerName+'@'+CriticalAlarmsjnewQueueName+'')
  target = cmo.getDestinationInfo()
  print 'Got the target...'
   
  cd('ServerServices/'+CriticalAlarmsjoldServerName+'/RuntimeService/ServerRuntime/'+CriticalAlarmsjoldServerName+'/JMSRuntime/'+CriticalAlarmsjoldServerName+'.jms/JMSServers/'+CriticalAlarmsjoldJmsServerName+'/Destinations/'+systemModuleName +'!'+CriticalAlarmsjoldJmsServerName+'@'+CriticalAlarmsjoldQueueName+'')
   
  print 'Moving the messages to the new target...'
  cmo.moveMessages('',target)
  print 'Messages have been moved to the target Successfully !!!'
   
  print '======================================='
  print 'Messages from queue: "'+CriticalAlarmsjoldQueueName+'" of "'+CriticalAlarmsjoldServerName+'"have been moved to the new queue: "'+CriticalAlarmsjnewQueueName+'" of "'+CriticalAlarmsjnewTargetedServerName+'"Successfully !!!'
  print '======================================='
  
  
  print 'Getting the target...'
  cd('ServerServices/'+CriticalAlarmsknewTargetedServerName+'/RuntimeService/ServerRuntime/'+CriticalAlarmsknewTargetedServerName+'/JMSRuntime/'+CriticalAlarmsknewTargetedServerName+'.jms/JMSServers/'+CriticalAlarmsknewJmsServerName+'/Destinations/'+systemModuleName +'!'+CriticalAlarmsknewJmsServerName+'@'+CriticalAlarmsknewQueueName+'')
  target = cmo.getDestinationInfo()
  print 'Got the target...'
   
  cd('ServerServices/'+CriticalAlarmskoldServerName+'/RuntimeService/ServerRuntime/'+CriticalAlarmskoldServerName+'/JMSRuntime/'+CriticalAlarmskoldServerName+'.jms/JMSServers/'+CriticalAlarmskoldJmsServerName+'/Destinations/'+systemModuleName +'!'+CriticalAlarmskoldJmsServerName+'@'+CriticalAlarmskoldQueueName+'')
   
  print 'Moving the messages to the new target...'
  cmo.moveMessages('',target)
  print 'Messages have been moved to the target Successfully !!!'
   
  print '======================================='
  print 'Messages from queue: "'+CriticalAlarmskoldQueueName+'" of "'+CriticalAlarmskoldServerName+'"have been moved to the new queue: "'+CriticalAlarmsknewQueueName+'" of "'+CriticalAlarmsknewTargetedServerName+'"Successfully !!!'
  print '======================================='
  
  
  print 'Getting the target...'
  cd('ServerServices/'+CriticalAlarmslnewTargetedServerName+'/RuntimeService/ServerRuntime/'+CriticalAlarmslnewTargetedServerName+'/JMSRuntime/'+CriticalAlarmslnewTargetedServerName+'.jms/JMSServers/'+CriticalAlarmslnewJmsServerName+'/Destinations/'+systemModuleName +'!'+CriticalAlarmslnewJmsServerName+'@'+CriticalAlarmslnewQueueName+'')
  target = cmo.getDestinationInfo()
  print 'Got the target...'
   
  cd('ServerServices/'+CriticalAlarmsloldServerName+'/RuntimeService/ServerRuntime/'+CriticalAlarmsloldServerName+'/JMSRuntime/'+CriticalAlarmsloldServerName+'.jms/JMSServers/'+CriticalAlarmsloldJmsServerName+'/Destinations/'+systemModuleName +'!'+CriticalAlarmsloldJmsServerName+'@'+CriticalAlarmsloldQueueName+'')
   
  print 'Moving the messages to the new target...'
  cmo.moveMessages('',target)
  print 'Messages have been moved to the target Successfully !!!'
   
  print '======================================='
  print 'Messages from queue: "'+CriticalAlarmsloldQueueName+'" of "'+CriticalAlarmsloldServerName+'"have been moved to the new queue: "'+CriticalAlarmslnewQueueName+'" of "'+CriticalAlarmslnewTargetedServerName+'"Successfully !!!'
  print '======================================='
  
  
  print 'Getting the target...'
  cd('ServerServices/'+CriticalAlarmsmnewTargetedServerName+'/RuntimeService/ServerRuntime/'+CriticalAlarmsmnewTargetedServerName+'/JMSRuntime/'+CriticalAlarmsmnewTargetedServerName+'.jms/JMSServers/'+CriticalAlarmsmnewJmsServerName+'/Destinations/'+systemModuleName +'!'+CriticalAlarmsmnewJmsServerName+'@'+CriticalAlarmsmnewQueueName+'')
  target = cmo.getDestinationInfo()
  print 'Got the target...'
   
  cd('ServerServices/'+CriticalAlarmsmoldServerName+'/RuntimeService/ServerRuntime/'+CriticalAlarmsmoldServerName+'/JMSRuntime/'+CriticalAlarmsmoldServerName+'.jms/JMSServers/'+CriticalAlarmsmoldJmsServerName+'/Destinations/'+systemModuleName +'!'+CriticalAlarmsmoldJmsServerName+'@'+CriticalAlarmsmoldQueueName+'')
   
  print 'Moving the messages to the new target...'
  cmo.moveMessages('',target)
  print 'Messages have been moved to the target Successfully !!!'
   
  print '======================================='
  print 'Messages from queue: "'+CriticalAlarmsmoldQueueName+'" of "'+CriticalAlarmsmoldServerName+'"have been moved to the new queue: "'+CriticalAlarmsmnewQueueName+'" of "'+CriticalAlarmsmnewTargetedServerName+'"Successfully !!!'
  print '======================================='
  
  
  print 'Getting the target...'
  cd('ServerServices/'+CriticalAlarmsnnewTargetedServerName+'/RuntimeService/ServerRuntime/'+CriticalAlarmsnnewTargetedServerName+'/JMSRuntime/'+CriticalAlarmsnnewTargetedServerName+'.jms/JMSServers/'+CriticalAlarmsnnewJmsServerName+'/Destinations/'+systemModuleName +'!'+CriticalAlarmsnnewJmsServerName+'@'+CriticalAlarmsnnewQueueName+'')
  target = cmo.getDestinationInfo()
  print 'Got the target...'
   
  cd('ServerServices/'+CriticalAlarmsnoldServerName+'/RuntimeService/ServerRuntime/'+CriticalAlarmsnoldServerName+'/JMSRuntime/'+CriticalAlarmsnoldServerName+'.jms/JMSServers/'+CriticalAlarmsnoldJmsServerName+'/Destinations/'+systemModuleName +'!'+CriticalAlarmsnoldJmsServerName+'@'+CriticalAlarmsnoldQueueName+'')
   
  print 'Moving the messages to the new target...'
  cmo.moveMessages('',target)
  print 'Messages have been moved to the target Successfully !!!'
   
  print '======================================='
  print 'Messages from queue: "'+CriticalAlarmsnoldQueueName+'" of "'+CriticalAlarmsnoldServerName+'"have been moved to the new queue: "'+CriticalAlarmsnnewQueueName+'" of "'+CriticalAlarmsnnewTargetedServerName+'"Successfully !!!'
  print '======================================='
  
  
  print 'Getting the target...'
  cd('ServerServices/'+CriticalAlarmsonewTargetedServerName+'/RuntimeService/ServerRuntime/'+CriticalAlarmsonewTargetedServerName+'/JMSRuntime/'+CriticalAlarmsonewTargetedServerName+'.jms/JMSServers/'+CriticalAlarmsonewJmsServerName+'/Destinations/'+systemModuleName +'!'+CriticalAlarmsonewJmsServerName+'@'+CriticalAlarmsonewQueueName+'')
  target = cmo.getDestinationInfo()
  print 'Got the target...'
   
  cd('ServerServices/'+CriticalAlarmsooldServerName+'/RuntimeService/ServerRuntime/'+CriticalAlarmsooldServerName+'/JMSRuntime/'+CriticalAlarmsooldServerName+'.jms/JMSServers/'+CriticalAlarmsooldJmsServerName+'/Destinations/'+systemModuleName +'!'+CriticalAlarmsooldJmsServerName+'@'+CriticalAlarmsooldQueueName+'')
   
  print 'Moving the messages to the new target...'
  cmo.moveMessages('',target)
  print 'Messages have been moved to the target Successfully !!!'
   
  print '======================================='
  print 'Messages from queue: "'+CriticalAlarmsooldQueueName+'" of "'+CriticalAlarmsooldServerName+'"have been moved to the new queue: "'+CriticalAlarmsonewQueueName+'" of "'+CriticalAlarmsonewTargetedServerName+'"Successfully !!!'
  print '======================================='
 except (SyntaxError, NameError, AttributeError, ValueError, WLSTException):
  print 'ignore error'
 exit()








