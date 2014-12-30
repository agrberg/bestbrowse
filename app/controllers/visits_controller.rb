class VisitsController < ApplicationController
  def create
    render json: Visit.create(visit_params)
  end

  private def visit_params
    params[:visit_at] = Time.parse(params[:visit_at])
    params.permit :url, :visit_at, :title, :visit_count
  end
end
