#
# Config file for SUMOS
#

# should use kafka for config changes (else it uses json file)
kafkaUpdates = True
# the kafka host we want to send our messages to
kafkaHost = "kafka:9092"

mqttUpdates = False
mqttHost = "localhost"
mqttPort = "1883"

# the topic we send the kafka messages to
kafkaTopicTrips = "crowd-nav-trips"
kafkaTopicPerformance = "crowd-nav-performance"
kafkaTopicRouting = "crowd-nav-routing"

# where we receive system changes
kafkaCommandsTopic = "crowd-nav-commands"

# True if we want to use the SUMO GUI (always of in parallel mode)
sumoUseGUI = True  # False

# The network config (links to the net) we use for our simulation
sumoConfig = "./app/map/eichstaedt.sumo.cfg"

# The network net we use for our simulation
sumoNet = "./app/map/eichstaedt.net.xml"

# Initial wait time before publishing overheads
initialWaitTicks = 200

# the total number of cars we use in our simulation
totalCarCounter = 750

smartCarCounter = 150

# percentage of cars that are smart
# DEPRECATED - USE smartCarCounter instead
smartCarPercentage = 0.2

# output variables to be used by OEDA
outputVariable1 = "overhead"
outputVariable2 = "complaint"
outputVariable3 = "minimalCosts"

# variables that are forwarded to crowd-nav-performance and crowd-nav-routing topics, respectively
dataProviderVariable1 = "lastTickDuration"
dataProviderVariable2 = "routingDuration"

# runtime dependent variable
processID = 0
parallelMode = False
