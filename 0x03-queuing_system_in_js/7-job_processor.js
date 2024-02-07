const kue = require('kue');
const queue = kue.createQueue();

const blacklistedNumbers = ['4153518780', '4153518781'];

function sendNotification(phoneNumber, message, job, done) {
  job.progress(0);
  if (blacklistedNumbers.includes(phoneNumber)) {
  	const error = new Error(`Phone number ${phoneNumber} is blacklisted`);
  	done(error);
  }
  job.progress(50);
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
  setTimeout(() => {
    job.progress(100);
  	done();
  }, 2000);
}

queue.process('push_notification_code_2', 2, (job, done) => {
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message, job, done);
});