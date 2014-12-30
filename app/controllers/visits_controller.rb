class VisitsController < ApplicationController
  def index
    @visits = Visit.all
  end

  def create
    render json: Visit.create(visit_params)
  end

  private def visit_params
    params[:visit_at] = Time.parse(params[:visit_at])
    params.permit :url, :visit_at, :title, :visit_count, :email, :browser_type, :browser_id
  end
end
