@Library('cloudops')
import com.bose.cloudops.*

def cloudops = new CloudOps(this)
cloudops.slackChannelName = "#dom-docker-intro-ops-"

node {
  // Process and execute the galapagos.yaml flow
  cloudops.executeMatrixBasedFlow()
}
