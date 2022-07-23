from java.io import FileInputStream
import java.lang
import os
import string
 
propInputStream = FileInputStream("/u02/jms_messagesmove/domain.propertiesOnlineROList")
configProps = Properties()
configProps.load(propInputStream)
 
serverUrl = configProps.get("server.url")
Username = configProps.get("username")
Password = configProps.get("password")
 
systemModuleName = configProps.get("system.module.name")
 
OnlineROListaoldServerName = configProps.get("OnlineROList.a.old.server.name")
OnlineROListaoldJmsServerName = configProps.get("OnlineROList.a.old.jms.server.name")
OnlineROListaoldQueueName = configProps.get("OnlineROList.a.old.queue.name")
 
OnlineROListanewTargetedServerName = configProps.get("OnlineROList.a.new.targeted.server.name")
OnlineROListanewJmsServerName = configProps.get("OnlineROList.a.new.jms.server.name")
OnlineROListanewQueueName = configProps.get("OnlineROList.a.new.queue.name")

OnlineROListboldServerName = configProps.get("OnlineROList.b.old.server.name")
OnlineROListboldJmsServerName = configProps.get("OnlineROList.b.old.jms.server.name")
OnlineROListboldQueueName = configProps.get("OnlineROList.b.old.queue.name")
 
OnlineROListbnewTargetedServerName = configProps.get("OnlineROList.b.new.targeted.server.name")
OnlineROListbnewJmsServerName = configProps.get("OnlineROList.b.new.jms.server.name")
OnlineROListbnewQueueName = configProps.get("OnlineROList.b.new.queue.name")

OnlineROListcoldServerName = configProps.get("OnlineROList.c.old.server.name")
OnlineROListcoldJmsServerName = configProps.get("OnlineROList.c.old.jms.server.name")
OnlineROListcoldQueueName = configProps.get("OnlineROList.c.old.queue.name")
 
OnlineROListcnewTargetedServerName = configProps.get("OnlineROList.c.new.targeted.server.name")
OnlineROListcnewJmsServerName = configProps.get("OnlineROList.c.new.jms.server.name")
OnlineROListcnewQueueName = configProps.get("OnlineROList.c.new.queue.name")

OnlineROListdoldServerName = configProps.get("OnlineROList.d.old.server.name")
OnlineROListdoldJmsServerName = configProps.get("OnlineROList.d.old.jms.server.name")
OnlineROListdoldQueueName = configProps.get("OnlineROList.d.old.queue.name")
 
OnlineROListdnewTargetedServerName = configProps.get("OnlineROList.d.new.targeted.server.name")
OnlineROListdnewJmsServerName = configProps.get("OnlineROList.d.new.jms.server.name")
OnlineROListdnewQueueName = configProps.get("OnlineROList.d.new.queue.name")

OnlineROListeoldServerName = configProps.get("OnlineROList.e.old.server.name")
OnlineROListeoldJmsServerName = configProps.get("OnlineROList.e.old.jms.server.name")
OnlineROListeoldQueueName = configProps.get("OnlineROList.e.old.queue.name")
 
OnlineROListenewTargetedServerName = configProps.get("OnlineROList.e.new.targeted.server.name")
OnlineROListenewJmsServerName = configProps.get("OnlineROList.e.new.jms.server.name")
OnlineROListenewQueueName = configProps.get("OnlineROList.e.new.queue.name")

OnlineROListfoldServerName = configProps.get("OnlineROList.f.old.server.name")
OnlineROListfoldJmsServerName = configProps.get("OnlineROList.f.old.jms.server.name")
OnlineROListfoldQueueName = configProps.get("OnlineROList.f.old.queue.name")
 
OnlineROListfnewTargetedServerName = configProps.get("OnlineROList.f.new.targeted.server.name")
OnlineROListfnewJmsServerName = configProps.get("OnlineROList.f.new.jms.server.name")
OnlineROListfnewQueueName = configProps.get("OnlineROList.f.new.queue.name")


OnlineROListgoldServerName = configProps.get("OnlineROList.g.old.server.name")
OnlineROListgoldJmsServerName = configProps.get("OnlineROList.g.old.jms.server.name")
OnlineROListgoldQueueName = configProps.get("OnlineROList.g.old.queue.name")
OnlineROListgnewTargetedServerName = configProps.get("OnlineROList.g.new.targeted.server.name")
OnlineROListgnewJmsServerName = configProps.get("OnlineROList.g.new.jms.server.name")
OnlineROListgnewQueueName = configProps.get("OnlineROList.g.new.queue.name")
OnlineROListholdServerName = configProps.get("OnlineROList.h.old.server.name")
OnlineROListholdJmsServerName = configProps.get("OnlineROList.h.old.jms.server.name")
OnlineROListholdQueueName = configProps.get("OnlineROList.h.old.queue.name")
OnlineROListhnewTargetedServerName = configProps.get("OnlineROList.h.new.targeted.server.name")
OnlineROListhnewJmsServerName = configProps.get("OnlineROList.h.new.jms.server.name")
OnlineROListhnewQueueName = configProps.get("OnlineROList.h.new.queue.name")
OnlineROListioldServerName = configProps.get("OnlineROList.i.old.server.name")
OnlineROListioldJmsServerName = configProps.get("OnlineROList.i.old.jms.server.name")
OnlineROListioldQueueName = configProps.get("OnlineROList.i.old.queue.name")
OnlineROListinewTargetedServerName = configProps.get("OnlineROList.i.new.targeted.server.name")
OnlineROListinewJmsServerName = configProps.get("OnlineROList.i.new.jms.server.name")
OnlineROListinewQueueName = configProps.get("OnlineROList.i.new.queue.name")
OnlineROListjoldServerName = configProps.get("OnlineROList.j.old.server.name")
OnlineROListjoldJmsServerName = configProps.get("OnlineROList.j.old.jms.server.name")
OnlineROListjoldQueueName = configProps.get("OnlineROList.j.old.queue.name")
OnlineROListjnewTargetedServerName = configProps.get("OnlineROList.j.new.targeted.server.name")
OnlineROListjnewJmsServerName = configProps.get("OnlineROList.j.new.jms.server.name")
OnlineROListjnewQueueName = configProps.get("OnlineROList.j.new.queue.name")
OnlineROListkoldServerName = configProps.get("OnlineROList.k.old.server.name")
OnlineROListkoldJmsServerName = configProps.get("OnlineROList.k.old.jms.server.name")
OnlineROListkoldQueueName = configProps.get("OnlineROList.k.old.queue.name")
OnlineROListknewTargetedServerName = configProps.get("OnlineROList.k.new.targeted.server.name")
OnlineROListknewJmsServerName = configProps.get("OnlineROList.k.new.jms.server.name")
OnlineROListknewQueueName = configProps.get("OnlineROList.k.new.queue.name")
OnlineROListloldServerName = configProps.get("OnlineROList.l.old.server.name")
OnlineROListloldJmsServerName = configProps.get("OnlineROList.l.old.jms.server.name")
OnlineROListloldQueueName = configProps.get("OnlineROList.l.old.queue.name")
OnlineROListlnewTargetedServerName = configProps.get("OnlineROList.l.new.targeted.server.name")
OnlineROListlnewJmsServerName = configProps.get("OnlineROList.l.new.jms.server.name")
OnlineROListlnewQueueName = configProps.get("OnlineROList.l.new.queue.name")
OnlineROListmoldServerName = configProps.get("OnlineROList.m.old.server.name")
OnlineROListmoldJmsServerName = configProps.get("OnlineROList.m.old.jms.server.name")
OnlineROListmoldQueueName = configProps.get("OnlineROList.m.old.queue.name")
OnlineROListmnewTargetedServerName = configProps.get("OnlineROList.m.new.targeted.server.name")
OnlineROListmnewJmsServerName = configProps.get("OnlineROList.m.new.jms.server.name")
OnlineROListmnewQueueName = configProps.get("OnlineROList.m.new.queue.name")
OnlineROListnoldServerName = configProps.get("OnlineROList.n.old.server.name")
OnlineROListnoldJmsServerName = configProps.get("OnlineROList.n.old.jms.server.name")
OnlineROListnoldQueueName = configProps.get("OnlineROList.n.old.queue.name")
OnlineROListnnewTargetedServerName = configProps.get("OnlineROList.n.new.targeted.server.name")
OnlineROListnnewJmsServerName = configProps.get("OnlineROList.n.new.jms.server.name")
OnlineROListnnewQueueName = configProps.get("OnlineROList.n.new.queue.name")
OnlineROListooldServerName = configProps.get("OnlineROList.o.old.server.name")
OnlineROListooldJmsServerName = configProps.get("OnlineROList.o.old.jms.server.name")
OnlineROListooldQueueName = configProps.get("OnlineROList.o.old.queue.name")
OnlineROListonewTargetedServerName = configProps.get("OnlineROList.o.new.targeted.server.name")
OnlineROListonewJmsServerName = configProps.get("OnlineROList.o.new.jms.server.name")
OnlineROListonewQueueName = configProps.get("OnlineROList.o.new.queue.name")


 
 
 
connect(userConfigFile=Username,userKeyFile=Password,url=serverUrl)
 
domainRuntime()

while True:
 try:
 
  print 'Getting the target...'
  cd('ServerServices/'+OnlineROListanewTargetedServerName+'/RuntimeService/ServerRuntime/'+OnlineROListanewTargetedServerName+'/JMSRuntime/'+OnlineROListanewTargetedServerName+'.jms/JMSServers/'+OnlineROListanewJmsServerName+'/Destinations/'+systemModuleName +'!'+OnlineROListanewJmsServerName+'@'+OnlineROListanewQueueName+'')
  target = cmo.getDestinationInfo()
  print 'Got the target...'
   
  cd('ServerServices/'+OnlineROListaoldServerName+'/RuntimeService/ServerRuntime/'+OnlineROListaoldServerName+'/JMSRuntime/'+OnlineROListaoldServerName+'.jms/JMSServers/'+OnlineROListaoldJmsServerName+'/Destinations/'+systemModuleName +'!'+OnlineROListaoldJmsServerName+'@'+OnlineROListaoldQueueName+'')
   
  print 'Moving the messages to the new target...'
  cmo.moveMessages('',target)
  print 'Messages have been moved to the target Successfully !!!'
   
  print '======================================='
  print 'Messages from queue: "'+OnlineROListaoldQueueName+'" of "'+OnlineROListaoldServerName+'"have been moved to the new queue: "'+OnlineROListanewQueueName+'" of "'+OnlineROListanewTargetedServerName+'"Successfully !!!'
  print '======================================='
  
  
  print 'Getting the target...'
  cd('ServerServices/'+OnlineROListbnewTargetedServerName+'/RuntimeService/ServerRuntime/'+OnlineROListbnewTargetedServerName+'/JMSRuntime/'+OnlineROListbnewTargetedServerName+'.jms/JMSServers/'+OnlineROListbnewJmsServerName+'/Destinations/'+systemModuleName +'!'+OnlineROListbnewJmsServerName+'@'+OnlineROListbnewQueueName+'')
  target = cmo.getDestinationInfo()
  print 'Got the target...'
   
  cd('ServerServices/'+OnlineROListboldServerName+'/RuntimeService/ServerRuntime/'+OnlineROListboldServerName+'/JMSRuntime/'+OnlineROListboldServerName+'.jms/JMSServers/'+OnlineROListboldJmsServerName+'/Destinations/'+systemModuleName +'!'+OnlineROListboldJmsServerName+'@'+OnlineROListboldQueueName+'')
   
  print 'Moving the messages to the new target...'
  cmo.moveMessages('',target)
  print 'Messages have been moved to the target Successfully !!!'
   
  print '======================================='
  print 'Messages from queue: "'+OnlineROListboldQueueName+'" of "'+OnlineROListboldServerName+'"have been moved to the new queue: "'+OnlineROListbnewQueueName+'" of "'+OnlineROListbnewTargetedServerName+'"Successfully !!!'
  print '======================================='
  
  
  print 'Getting the target...'
  cd('ServerServices/'+OnlineROListcnewTargetedServerName+'/RuntimeService/ServerRuntime/'+OnlineROListcnewTargetedServerName+'/JMSRuntime/'+OnlineROListcnewTargetedServerName+'.jms/JMSServers/'+OnlineROListcnewJmsServerName+'/Destinations/'+systemModuleName +'!'+OnlineROListcnewJmsServerName+'@'+OnlineROListcnewQueueName+'')
  target = cmo.getDestinationInfo()
  print 'Got the target...'
   
  cd('ServerServices/'+OnlineROListcoldServerName+'/RuntimeService/ServerRuntime/'+OnlineROListcoldServerName+'/JMSRuntime/'+OnlineROListcoldServerName+'.jms/JMSServers/'+OnlineROListcoldJmsServerName+'/Destinations/'+systemModuleName +'!'+OnlineROListcoldJmsServerName+'@'+OnlineROListcoldQueueName+'')
   
  print 'Moving the messages to the new target...'
  cmo.moveMessages('',target)
  print 'Messages have been moved to the target Successfully !!!'
   
  print '======================================='
  print 'Messages from queue: "'+OnlineROListcoldQueueName+'" of "'+OnlineROListcoldServerName+'"have been moved to the new queue: "'+OnlineROListcnewQueueName+'" of "'+OnlineROListcnewTargetedServerName+'"Successfully !!!'
  print '======================================='
  
  
  print 'Getting the target...'
  cd('ServerServices/'+OnlineROListdnewTargetedServerName+'/RuntimeService/ServerRuntime/'+OnlineROListdnewTargetedServerName+'/JMSRuntime/'+OnlineROListdnewTargetedServerName+'.jms/JMSServers/'+OnlineROListdnewJmsServerName+'/Destinations/'+systemModuleName +'!'+OnlineROListdnewJmsServerName+'@'+OnlineROListdnewQueueName+'')
  target = cmo.getDestinationInfo()
  print 'Got the target...'
   
  cd('ServerServices/'+OnlineROListdoldServerName+'/RuntimeService/ServerRuntime/'+OnlineROListdoldServerName+'/JMSRuntime/'+OnlineROListdoldServerName+'.jms/JMSServers/'+OnlineROListdoldJmsServerName+'/Destinations/'+systemModuleName +'!'+OnlineROListdoldJmsServerName+'@'+OnlineROListdoldQueueName+'')
   
  print 'Moving the messages to the new target...'
  cmo.moveMessages('',target)
  print 'Messages have been moved to the target Successfully !!!'
   
  print '======================================='
  print 'Messages from queue: "'+OnlineROListdoldQueueName+'" of "'+OnlineROListdoldServerName+'"have been moved to the new queue: "'+OnlineROListdnewQueueName+'" of "'+OnlineROListdnewTargetedServerName+'"Successfully !!!'
  print '======================================='
  
  
  print 'Getting the target...'
  cd('ServerServices/'+OnlineROListenewTargetedServerName+'/RuntimeService/ServerRuntime/'+OnlineROListenewTargetedServerName+'/JMSRuntime/'+OnlineROListenewTargetedServerName+'.jms/JMSServers/'+OnlineROListenewJmsServerName+'/Destinations/'+systemModuleName +'!'+OnlineROListenewJmsServerName+'@'+OnlineROListenewQueueName+'')
  target = cmo.getDestinationInfo()
  print 'Got the target...'
   
  cd('ServerServices/'+OnlineROListeoldServerName+'/RuntimeService/ServerRuntime/'+OnlineROListeoldServerName+'/JMSRuntime/'+OnlineROListeoldServerName+'.jms/JMSServers/'+OnlineROListeoldJmsServerName+'/Destinations/'+systemModuleName +'!'+OnlineROListeoldJmsServerName+'@'+OnlineROListeoldQueueName+'')
   
  print 'Moving the messages to the new target...'
  cmo.moveMessages('',target)
  print 'Messages have been moved to the target Successfully !!!'
   
  print '======================================='
  print 'Messages from queue: "'+OnlineROListeoldQueueName+'" of "'+OnlineROListeoldServerName+'"have been moved to the new queue: "'+OnlineROListenewQueueName+'" of "'+OnlineROListenewTargetedServerName+'"Successfully !!!'
  print '======================================='
  
  
  print 'Getting the target...'
  cd('ServerServices/'+OnlineROListfnewTargetedServerName+'/RuntimeService/ServerRuntime/'+OnlineROListfnewTargetedServerName+'/JMSRuntime/'+OnlineROListfnewTargetedServerName+'.jms/JMSServers/'+OnlineROListfnewJmsServerName+'/Destinations/'+systemModuleName +'!'+OnlineROListfnewJmsServerName+'@'+OnlineROListfnewQueueName+'')
  target = cmo.getDestinationInfo()
  print 'Got the target...'
   
  cd('ServerServices/'+OnlineROListfoldServerName+'/RuntimeService/ServerRuntime/'+OnlineROListfoldServerName+'/JMSRuntime/'+OnlineROListfoldServerName+'.jms/JMSServers/'+OnlineROListfoldJmsServerName+'/Destinations/'+systemModuleName +'!'+OnlineROListfoldJmsServerName+'@'+OnlineROListfoldQueueName+'')
   
  print 'Moving the messages to the new target...'
  cmo.moveMessages('',target)
  print 'Messages have been moved to the target Successfully !!!'
   
  print '======================================='
  print 'Messages from queue: "'+OnlineROListfoldQueueName+'" of "'+OnlineROListfoldServerName+'"have been moved to the new queue: "'+OnlineROListfnewQueueName+'" of "'+OnlineROListfnewTargetedServerName+'"Successfully !!!'
  print '======================================='
  
  print 'Getting the target...'
  cd('ServerServices/'+OnlineROListgnewTargetedServerName+'/RuntimeService/ServerRuntime/'+OnlineROListgnewTargetedServerName+'/JMSRuntime/'+OnlineROListgnewTargetedServerName+'.jms/JMSServers/'+OnlineROListgnewJmsServerName+'/Destinations/'+systemModuleName +'!'+OnlineROListgnewJmsServerName+'@'+OnlineROListgnewQueueName+'')
  target = cmo.getDestinationInfo()
  print 'Got the target...'
   
  cd('ServerServices/'+OnlineROListgoldServerName+'/RuntimeService/ServerRuntime/'+OnlineROListgoldServerName+'/JMSRuntime/'+OnlineROListgoldServerName+'.jms/JMSServers/'+OnlineROListgoldJmsServerName+'/Destinations/'+systemModuleName +'!'+OnlineROListgoldJmsServerName+'@'+OnlineROListgoldQueueName+'')
   
  print 'Moving the messages to the new target...'
  cmo.moveMessages('',target)
  print 'Messages have been moved to the target Successfully !!!'
   
  print '======================================='
  print 'Messages from queue: "'+OnlineROListgoldQueueName+'" of "'+OnlineROListgoldServerName+'"have been moved to the new queue: "'+OnlineROListgnewQueueName+'" of "'+OnlineROListgnewTargetedServerName+'"Successfully !!!'
  print '======================================='
  
  print 'Getting the target...'
  cd('ServerServices/'+OnlineROListhnewTargetedServerName+'/RuntimeService/ServerRuntime/'+OnlineROListhnewTargetedServerName+'/JMSRuntime/'+OnlineROListhnewTargetedServerName+'.jms/JMSServers/'+OnlineROListhnewJmsServerName+'/Destinations/'+systemModuleName +'!'+OnlineROListhnewJmsServerName+'@'+OnlineROListhnewQueueName+'')
  target = cmo.getDestinationInfo()
  print 'Got the target...'
   
  cd('ServerServices/'+OnlineROListholdServerName+'/RuntimeService/ServerRuntime/'+OnlineROListholdServerName+'/JMSRuntime/'+OnlineROListholdServerName+'.jms/JMSServers/'+OnlineROListholdJmsServerName+'/Destinations/'+systemModuleName +'!'+OnlineROListholdJmsServerName+'@'+OnlineROListholdQueueName+'')
   
  print 'Moving the messages to the new target...'
  cmo.moveMessages('',target)
  print 'Messages have been moved to the target Successfully !!!'
   
  print '======================================='
  print 'Messages from queue: "'+OnlineROListholdQueueName+'" of "'+OnlineROListholdServerName+'"have been moved to the new queue: "'+OnlineROListhnewQueueName+'" of "'+OnlineROListhnewTargetedServerName+'"Successfully !!!'
  print '======================================='
  
  
  print 'Getting the target...'
  cd('ServerServices/'+OnlineROListinewTargetedServerName+'/RuntimeService/ServerRuntime/'+OnlineROListinewTargetedServerName+'/JMSRuntime/'+OnlineROListinewTargetedServerName+'.jms/JMSServers/'+OnlineROListinewJmsServerName+'/Destinations/'+systemModuleName +'!'+OnlineROListinewJmsServerName+'@'+OnlineROListinewQueueName+'')
  target = cmo.getDestinationInfo()
  print 'Got the target...'
   
  cd('ServerServices/'+OnlineROListioldServerName+'/RuntimeService/ServerRuntime/'+OnlineROListioldServerName+'/JMSRuntime/'+OnlineROListioldServerName+'.jms/JMSServers/'+OnlineROListioldJmsServerName+'/Destinations/'+systemModuleName +'!'+OnlineROListioldJmsServerName+'@'+OnlineROListioldQueueName+'')
   
  print 'Moving the messages to the new target...'
  cmo.moveMessages('',target)
  print 'Messages have been moved to the target Successfully !!!'
   
  print '======================================='
  print 'Messages from queue: "'+OnlineROListioldQueueName+'" of "'+OnlineROListioldServerName+'"have been moved to the new queue: "'+OnlineROListinewQueueName+'" of "'+OnlineROListinewTargetedServerName+'"Successfully !!!'
  print '======================================='
  
  
  print 'Getting the target...'
  cd('ServerServices/'+OnlineROListjnewTargetedServerName+'/RuntimeService/ServerRuntime/'+OnlineROListjnewTargetedServerName+'/JMSRuntime/'+OnlineROListjnewTargetedServerName+'.jms/JMSServers/'+OnlineROListjnewJmsServerName+'/Destinations/'+systemModuleName +'!'+OnlineROListjnewJmsServerName+'@'+OnlineROListjnewQueueName+'')
  target = cmo.getDestinationInfo()
  print 'Got the target...'
   
  cd('ServerServices/'+OnlineROListjoldServerName+'/RuntimeService/ServerRuntime/'+OnlineROListjoldServerName+'/JMSRuntime/'+OnlineROListjoldServerName+'.jms/JMSServers/'+OnlineROListjoldJmsServerName+'/Destinations/'+systemModuleName +'!'+OnlineROListjoldJmsServerName+'@'+OnlineROListjoldQueueName+'')
   
  print 'Moving the messages to the new target...'
  cmo.moveMessages('',target)
  print 'Messages have been moved to the target Successfully !!!'
   
  print '======================================='
  print 'Messages from queue: "'+OnlineROListjoldQueueName+'" of "'+OnlineROListjoldServerName+'"have been moved to the new queue: "'+OnlineROListjnewQueueName+'" of "'+OnlineROListjnewTargetedServerName+'"Successfully !!!'
  print '======================================='
  
  
  print 'Getting the target...'
  cd('ServerServices/'+OnlineROListknewTargetedServerName+'/RuntimeService/ServerRuntime/'+OnlineROListknewTargetedServerName+'/JMSRuntime/'+OnlineROListknewTargetedServerName+'.jms/JMSServers/'+OnlineROListknewJmsServerName+'/Destinations/'+systemModuleName +'!'+OnlineROListknewJmsServerName+'@'+OnlineROListknewQueueName+'')
  target = cmo.getDestinationInfo()
  print 'Got the target...'
   
  cd('ServerServices/'+OnlineROListkoldServerName+'/RuntimeService/ServerRuntime/'+OnlineROListkoldServerName+'/JMSRuntime/'+OnlineROListkoldServerName+'.jms/JMSServers/'+OnlineROListkoldJmsServerName+'/Destinations/'+systemModuleName +'!'+OnlineROListkoldJmsServerName+'@'+OnlineROListkoldQueueName+'')
   
  print 'Moving the messages to the new target...'
  cmo.moveMessages('',target)
  print 'Messages have been moved to the target Successfully !!!'
   
  print '======================================='
  print 'Messages from queue: "'+OnlineROListkoldQueueName+'" of "'+OnlineROListkoldServerName+'"have been moved to the new queue: "'+OnlineROListknewQueueName+'" of "'+OnlineROListknewTargetedServerName+'"Successfully !!!'
  print '======================================='
  
  
  print 'Getting the target...'
  cd('ServerServices/'+OnlineROListlnewTargetedServerName+'/RuntimeService/ServerRuntime/'+OnlineROListlnewTargetedServerName+'/JMSRuntime/'+OnlineROListlnewTargetedServerName+'.jms/JMSServers/'+OnlineROListlnewJmsServerName+'/Destinations/'+systemModuleName +'!'+OnlineROListlnewJmsServerName+'@'+OnlineROListlnewQueueName+'')
  target = cmo.getDestinationInfo()
  print 'Got the target...'
   
  cd('ServerServices/'+OnlineROListloldServerName+'/RuntimeService/ServerRuntime/'+OnlineROListloldServerName+'/JMSRuntime/'+OnlineROListloldServerName+'.jms/JMSServers/'+OnlineROListloldJmsServerName+'/Destinations/'+systemModuleName +'!'+OnlineROListloldJmsServerName+'@'+OnlineROListloldQueueName+'')
   
  print 'Moving the messages to the new target...'
  cmo.moveMessages('',target)
  print 'Messages have been moved to the target Successfully !!!'
   
  print '======================================='
  print 'Messages from queue: "'+OnlineROListloldQueueName+'" of "'+OnlineROListloldServerName+'"have been moved to the new queue: "'+OnlineROListlnewQueueName+'" of "'+OnlineROListlnewTargetedServerName+'"Successfully !!!'
  print '======================================='
  
  
  print 'Getting the target...'
  cd('ServerServices/'+OnlineROListmnewTargetedServerName+'/RuntimeService/ServerRuntime/'+OnlineROListmnewTargetedServerName+'/JMSRuntime/'+OnlineROListmnewTargetedServerName+'.jms/JMSServers/'+OnlineROListmnewJmsServerName+'/Destinations/'+systemModuleName +'!'+OnlineROListmnewJmsServerName+'@'+OnlineROListmnewQueueName+'')
  target = cmo.getDestinationInfo()
  print 'Got the target...'
   
  cd('ServerServices/'+OnlineROListmoldServerName+'/RuntimeService/ServerRuntime/'+OnlineROListmoldServerName+'/JMSRuntime/'+OnlineROListmoldServerName+'.jms/JMSServers/'+OnlineROListmoldJmsServerName+'/Destinations/'+systemModuleName +'!'+OnlineROListmoldJmsServerName+'@'+OnlineROListmoldQueueName+'')
   
  print 'Moving the messages to the new target...'
  cmo.moveMessages('',target)
  print 'Messages have been moved to the target Successfully !!!'
   
  print '======================================='
  print 'Messages from queue: "'+OnlineROListmoldQueueName+'" of "'+OnlineROListmoldServerName+'"have been moved to the new queue: "'+OnlineROListmnewQueueName+'" of "'+OnlineROListmnewTargetedServerName+'"Successfully !!!'
  print '======================================='
  
  
  print 'Getting the target...'
  cd('ServerServices/'+OnlineROListnnewTargetedServerName+'/RuntimeService/ServerRuntime/'+OnlineROListnnewTargetedServerName+'/JMSRuntime/'+OnlineROListnnewTargetedServerName+'.jms/JMSServers/'+OnlineROListnnewJmsServerName+'/Destinations/'+systemModuleName +'!'+OnlineROListnnewJmsServerName+'@'+OnlineROListnnewQueueName+'')
  target = cmo.getDestinationInfo()
  print 'Got the target...'
   
  cd('ServerServices/'+OnlineROListnoldServerName+'/RuntimeService/ServerRuntime/'+OnlineROListnoldServerName+'/JMSRuntime/'+OnlineROListnoldServerName+'.jms/JMSServers/'+OnlineROListnoldJmsServerName+'/Destinations/'+systemModuleName +'!'+OnlineROListnoldJmsServerName+'@'+OnlineROListnoldQueueName+'')
   
  print 'Moving the messages to the new target...'
  cmo.moveMessages('',target)
  print 'Messages have been moved to the target Successfully !!!'
   
  print '======================================='
  print 'Messages from queue: "'+OnlineROListnoldQueueName+'" of "'+OnlineROListnoldServerName+'"have been moved to the new queue: "'+OnlineROListnnewQueueName+'" of "'+OnlineROListnnewTargetedServerName+'"Successfully !!!'
  print '======================================='
  
  
  print 'Getting the target...'
  cd('ServerServices/'+OnlineROListonewTargetedServerName+'/RuntimeService/ServerRuntime/'+OnlineROListonewTargetedServerName+'/JMSRuntime/'+OnlineROListonewTargetedServerName+'.jms/JMSServers/'+OnlineROListonewJmsServerName+'/Destinations/'+systemModuleName +'!'+OnlineROListonewJmsServerName+'@'+OnlineROListonewQueueName+'')
  target = cmo.getDestinationInfo()
  print 'Got the target...'
   
  cd('ServerServices/'+OnlineROListooldServerName+'/RuntimeService/ServerRuntime/'+OnlineROListooldServerName+'/JMSRuntime/'+OnlineROListooldServerName+'.jms/JMSServers/'+OnlineROListooldJmsServerName+'/Destinations/'+systemModuleName +'!'+OnlineROListooldJmsServerName+'@'+OnlineROListooldQueueName+'')
   
  print 'Moving the messages to the new target...'
  cmo.moveMessages('',target)
  print 'Messages have been moved to the target Successfully !!!'
   
  print '======================================='
  print 'Messages from queue: "'+OnlineROListooldQueueName+'" of "'+OnlineROListooldServerName+'"have been moved to the new queue: "'+OnlineROListonewQueueName+'" of "'+OnlineROListonewTargetedServerName+'"Successfully !!!'
  print '======================================='
 except (SyntaxError, NameError, AttributeError, ValueError, WLSTException):
  print 'ignore error'
 exit()








