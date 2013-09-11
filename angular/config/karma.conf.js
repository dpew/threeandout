module.exports = function (config) {
  config.set({
    basePath: '../..',

    files: [
      'threeandout/test_stats/static/angular/app/lib/angular/angular.js',
      'threeandout/test_stats/static/angular/app/lib/angular/angular-*.js',
      'angular/test/lib/angular/angular-mocks.js',
      'threeandout/test_stats/static/angular/app/js/**/*.js',
      'angular/test/unit/**/*.js'
    ],

    frameworks: ['jasmine'],

    autoWatch: true,

    browsers: ['PhantomJS'],

    junitReporter: {
      outputFile: 'test_out/unit.xml',
      suite: 'unit'
    }
  });
};
