class VisitsController < ApplicationController
  def index
    @visits = Visit.order(id: :desc)
  end

  def create
    render json: Visit.create(visit_params)
  end

  private def visit_params
    params[:visit_at] = Time.parse(params[:visit_at])
    params[:base_url] = Visit.base_url_for(params[:url])
    params.permit :url, :visit_at, :title, :visit_count, :email, :browser_type, :browser_id, :base_url
  end
end
