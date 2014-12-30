class VisitsController < ApplicationController
  def create
    render json: Visit.create(visit_params)
  end

  private def visit_params
    params.permit :url, :visit_at
  end
end
