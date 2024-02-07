const kue = require('kue');
const queue = kue.createQueue();

function sendNotification(phonenumber, message) {
  console.log(`Sending notification to ${phonenumber}, with message: ${message}`);
}

queue.process('push_notification_code', (job, done) => {
  const { phonenumber, message } = job.data;
  sendNotification(phonenumber, message);
  done();
});