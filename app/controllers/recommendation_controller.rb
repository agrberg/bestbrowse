class RecommendationController < ApplicationController
  def index
    render json: 'http://www.google.com'
  end
end
