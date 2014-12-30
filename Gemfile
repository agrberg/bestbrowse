source 'https://rubygems.org'

ruby '2.1.5'

gem 'rails', '4.1.8'
gem 'pg', '~> 0.17'
gem 'sass-rails', '~> 4.0.3'
gem 'uglifier', '>= 1.3.0'
gem 'coffee-rails', '~> 4.0.0'

gem 'haml-rails'
gem 'jquery-rails'
gem 'turbolinks'
gem 'jbuilder', '~> 2.0'

gem 'unicorn'

group :doc do
  gem 'sdoc', '~> 0.4.0'
end

group :production do
  gem 'rails_12factor'
end

group :development do
  gem 'quiet_assets'
  gem 'spring' # Spring speeds up development by keeping your application running in the background. Read more: https://github.com/rails/spring
  gem 'thin'
end

group :test do
  gem 'capybara-webkit'
  gem 'cucumber-rails'
  gem 'database_cleaner', '~> 1.3.0'
  gem 'dill', github: 'mojotech/dill', branch: 'master'
end

group :development, :test do
  gem 'array_proc'
  gem 'dotenv-rails'
  gem 'pry-byebug'
  gem 'pry-rails'
  gem 'pry-stack_explorer'
  gem 'rspec-rails'
  gem 'string_proc'
end
