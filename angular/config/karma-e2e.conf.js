module.exports = function (config) {
  config.set({
    basePath: '../',

    files: [
      'test/e2e/**/*.js'
    ],

    frameworks: ['ng-scenario'],

    autoWatch: false,

    browsers: ['PhantomJS'],

    singleRun: true,

    proxies: {
      '/': 'http://localhost/aajs/'
    },

    junitReporter: {
      outputFile: 'test_out/e2e.xml',
      suite: 'e2e'
    }
  });
};
