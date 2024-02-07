const chai = require('chai');
const sinon = require('sinon');
const kue = require('kue');
const createPushNotificationsJobs = require('./8-job');

const expect = chai.expect;
const queue = kue.createQueue();

// Switch Kue to test mode
queue.testMode.enter();

// Sample jobs array for testing
const jobs = [
  {
    phoneNumber: '1234567890',
    message: 'Test message 1'
  },
  {
    phoneNumber: '9876543210',
    message: 'Test message 2'
  },
];

describe('createPushNotificationsJobs', () => {
  let saveSpy;

  beforeEach(() => {
    queue.testMode.clear();
    saveSpy = sinon.spy(kue.Job.prototype, 'save');
  });

  afterEach(() => {
    saveSpy.restore();
    queue.testMode.exit();
  });

  it('should create jobs in the queue and call save method', () => {
    createPushNotificationsJobs(jobs, queue);
    expect(queue.testMode.jobs.length).to.equal(jobs.length);
    expect(saveSpy.callCount).to.equal(jobs.length);

    jobs.forEach((jobData, index) => {
      const createdJob = queue.testMode.jobs[index];
      expect(createdJob.type).to.equal('push_notification_code_3');
      expect(createdJob.data).to.deep.equal(jobData);
    });
  });
});